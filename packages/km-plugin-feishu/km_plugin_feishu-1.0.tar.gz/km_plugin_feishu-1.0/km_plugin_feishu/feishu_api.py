import time
import uuid
from functools import wraps

import requests
from elasticsearch_dsl.query import Query
from km_sdk.api_provider import FileDto, PermissionDto, UserDto, ApiProvider
from km_sdk.utils.cache_utils import CacheUtils
from km_sdk.utils.log_utils import LogUtils
from km_sdk.utils.setting_utils import SettingUtils
from km_sdk.utils.webhook_utils import WebhookUtils

sync_logger = LogUtils.get_logger()


def decode_request(func):
    """
    返回json结构
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        result.raise_for_status()  # 检查请求是否成功
        result_json = result.json()
        if "code" in result_json and result_json['code'] != 0:
            error_message = result_json.get('msg') or result_json.get('message')
            raise PermissionError(f"PermissionError: {error_message}")
        if "data" in result_json:
            return result_json['data']
        return result_json

    return wrapper


def verify_token_decorator(func):
    @wraps(func)
    def wrapper(self: ApiProvider, *args, **kwargs):
        return func(self, *args, **kwargs)  # 执行原方法

    return wrapper


def get_codes(api_provider: ApiProvider):
    code = WebhookUtils.get_request_params().get("code")
    app_id = WebhookUtils.get_request_params().get("state")
    assert code, "code 为空"
    assert app_id, "state 为空"
    CacheUtils.set(app_id + "_code", code, 300)
    return 200, "text/html; charset=utf-8", "获取code成功,请点击保存重试"


def feishu_scope():
    return "+".join(['drive:drive.metadata:readonly',
                     'drive:drive:readonly',
                     'docx:document:readonly',
                     'wiki:wiki:readonly',
                     'drive:export:readonly',
                     'drive:file:download',
                     'contact:user.base:readonly',
                     'contact:contact.base:readonly'])


def get_file_extension(obj_type: str) -> str:
    if obj_type == "docx":
        return "docx"
    elif obj_type == "bitable":
        return "xlsx"
    elif obj_type == "sheet":
        return "xlsx"
    elif obj_type == "doc":
        return "doc"
    else:
        return "docx"


class FeiShuApi(ApiProvider):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.app_id = kwargs.get("app_id")
        self.app_secret = kwargs.get("app_secret")
        self.headers = {
            'accept': 'application/json',
            'charset': 'utf-8'
        }

    @verify_token_decorator
    def get_files(self, page_size=20, current=None) -> list[FileDto]:
        files = []
        processed_tokens = set()  # 用于记录已经处理过的文件和空间ID

        def add_file(file_data):
            """Helper function to add a file to the files list."""
            file_token = file_data.get("token", "")
            file_type = file_data.get("type", "")
            file_name = file_data.get("name", "")
            if file_type != "slides":
                file_id = f"{file_token}_{file_type}"
                f = FileDto({
                    "id": file_id,
                    "name": file_name,
                    'size': None,
                    "md5": None,
                })
                files.append(f)

        def create_file_dto(node):
            """Helper function to create FileDto from node data."""
            node_token = node.get("node_token", "")
            obj_token = node.get("obj_token", "")
            node_type = node.get("obj_type", "")
            if node_type != "slides":
                node_id = f"{node_token}_{node_type}_{obj_token}"
                return FileDto({
                    "id": node_id,
                    "name": node.get("title", ""),
                    'size': None,
                    "md5": None,
                })

        def fetch_files(folder_token):
            """Fetch files in a folder and handle pagination."""
            page_token = None
            while True:
                # 获取文件夹文件列表
                data = self.get_files_list(page_token=page_token, folder_token=folder_token)
                items = data.get("files", [])
                more = data.get("has_more")
                next_page_token = data.get("next_page_token")

                for item in items:
                    file_token = item.get("token", "")
                    if file_token in processed_tokens:
                        continue  # 如果已经处理过该文件，则跳过
                    processed_tokens.add(file_token)

                    if item.get("type") == "folder":
                        # 递归获取子文件夹中的文件
                        fetch_files(file_token)
                    else:
                        add_file(item)

                if not more:
                    break  # 如果没有更多数据，退出循环

                page_token = next_page_token

        def fetch_spaces(page_token):
            """Fetch knowledge spaces and their nodes."""
            while True:
                try:
                    # 调用 get_spaces 方法并传递 page_token, 获取知识空间列表
                    data = self.get_spaces(page_token)
                    items = data.get("items", [])
                    new_page_token = data.get("page_token", "")

                    for item in items:
                        space_id = item.get("space_id", "")
                        if space_id in processed_tokens:
                            continue  # 如果已经处理过该空间ID，则跳过

                        # 获取知识空间子节点列表
                        nodes_data = self.get_nodes(space_id)
                        nodes = nodes_data.get("items", [])

                        for node in nodes:
                            if node.get("has_child"):
                                sub_nodes = fetch_nodes(node.get("space_id"), node.get("node_token"))
                                for sub_node in sub_nodes:
                                    files.append(create_file_dto(sub_node))

                            files.append(create_file_dto(node))

                        processed_tokens.add(space_id)  # 标记该空间ID已处理

                    # 如果 new_page_token 为 "0||0" 且所有空间ID都已处理完毕，则终止
                    if new_page_token == "0||0" and len(processed_tokens) == len(items):
                        break

                        # 更新 page_token
                    page_token = new_page_token
                except Exception as e:
                    print(f"Error while fetching spaces: {e}")
                    break

        def fetch_nodes(space_id, node_token=None, page_token=None):
            """Fetch nodes for a given space or node, handling pagination."""
            all_nodes = []
            while True:
                # 获取节点列表
                data = self.get_nodes(space_id, node_token=node_token, page_token=page_token)
                items = data.get("items", [])
                more = data.get("has_more")

                all_nodes.extend(items)

                if not more:
                    break  # 如果没有更多数据，退出循环

                # 如果有更多数据，获取 next_page_token 并更新 page_token
                next_page_token = data.get("page_token")
                page_token = next_page_token

            return all_nodes

        # 先获取文件

        fetch_files(current)

        # 再获取知识空间
        fetch_spaces(None)  # 默认传入 None 获取知识空间的第一页

        return files

    @verify_token_decorator
    def get_file(self, file_id: str) -> FileDto:
        # 根据token获取当前文件信息
        parts = file_id.split("_")
        if len(parts) == 3:
            node_token, obj_type, obj_token = parts
            response = self.get_information_by_token(node_token)
            node_info = response.get("node", {})
            file_name = node_info.get("title", "")
            file_extension = get_file_extension(obj_type)
            f = FileDto({
                "id": file_id,
                "name": f"{file_name}.{file_extension}",
                'size': None,
                "md5": None,
            })
            return f
        elif len(parts) == 2:
            node_token, obj_type = parts
            response = self.get_file_information_by_token(node_token, obj_type)
            file_info_list = response.get("metas", [])
            if file_info_list:
                file_info = file_info_list[0]
            else:
                file_info = {}
            file_name = file_info.get("title", "")
            file_extension = get_file_extension(obj_type)
            f = FileDto({
                "id": file_id,
                "name": f"{file_name}.{file_extension}",
                'size': None,
                "md5": None,
            })
            return f

    @verify_token_decorator
    def download(self, file_id: str) -> bytes:
        # node_token, obj_type, obj_token = parts   知识库  ,  node_token, obj_type = parts  文件
        # 分割获取文件信息
        parts = file_id.split("_")

        obj_type = None  # 初始化为 None
        obj_token = None  # 初始化为 None

        if len(parts) == 3:
            # 处理形式为 id_type_token
            node_token, obj_type, obj_token = parts
        elif len(parts) == 2:
            # 处理形式为 id_type
            node_token, obj_type = parts
            obj_token = node_token

            #  区分类型
        if obj_type == "docx":
            file_extension = "docx"
        elif obj_type == "bitable":
            file_extension = "xlsx"
        elif obj_type == "sheet":
            file_extension = "xlsx"
        elif obj_type == "doc":
            file_extension = "docx"
        else:
            raise ValueError(f"Unsupported object type: {obj_type}")

        # 1.创建导出任务
        data = self.create_export_task(obj_token, obj_type, file_extension)
        ticket = data.get("ticket")
        fileToken = None
        # 2.查询导出任务结果
        for _ in range(3):  # 重试3次
            data = self.select_task_by_token(obj_token, ticket)
            fileToken = data.get("result", {}).get("file_token")
            if fileToken:
                break
            time.sleep(2)

        if not fileToken:
            raise RuntimeError("Failed to obtain file token after multiple attempts")
        # 3.下载导出文件
        response = self.download_task(fileToken)
        return response.content

    @verify_token_decorator
    def list_file_permission(self, file_id: str) -> [PermissionDto]:
        return []

    @verify_token_decorator
    def list_user_file_permission(self, user_id: str, file_ids: [str]) -> [str]:
        return []

    @verify_token_decorator
    def get_user(self, user_id: str) -> UserDto:
        # 自建应用通过授权之后,用户的id需要通过飞书文档中的获取登录用户信息获取open_id,再用open_id调以下
        data = self.get_information_by_id(user_id)

        datas = data.get("user", '{}')
        user_dto = UserDto(
            name=datas.get('name', ''),
            id=datas.get('open_id', ''),
            permissions=None
        )
        return user_dto

    @verify_token_decorator
    def build_filter(self, user_id: str, related_sync_system: str, bqry: Query) -> Query:
        return bqry

    def system_init(self):
        if not SettingUtils.get_setting(self, "refresh_token"):
            refresh_token = CacheUtils.get(self.app_id + "_refresh_token")
            assert refresh_token, "refresh_token not exists"
            SettingUtils.set_setting(self, "refresh_token", refresh_token)
            self.get_user_access_token()

    def test_connection(self):
        code = CacheUtils.get(self.app_id + "_code")
        if code:
            data = self._get_app_access_token()
            if data.get("code") != 0:
                raise ValueError(f"获取访问令牌失败:{data.get('msg')},请检查 app_id 或 app_secret 是否正确。")
            app_token = data.get("app_access_token")
            CacheUtils.set(self.app_id + "_code", code, expire=1)
            data = self._get_user_access_token(code, app_token)
            refresh_token = data.get("refresh_token")
            refresh_expire = data.get("refresh_expires_in")
            CacheUtils.set(self.app_id + "_refresh_token", refresh_token, expire=refresh_expire)
            return
        id = uuid.uuid1().hex
        self.related_sync_system = id + "_temp"
        redirect_url = WebhookUtils.add_webhook(self, "code", ["GET"], get_codes, self.related_sync_system + "_code")
        scope = feishu_scope()
        app_id = self.app_id

        def guide(*args, **kwargs):
            nonlocal redirect_url, app_id, scope
            redirect_url = redirect_url.replace("/v1/", "/api/")
            html = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>请按步骤操作</title>
  <script type="text/javascript">
      function get_redirect_url(){{
        return window.location.protocol+"//"+window.location.host+"{redirect_url}"
      }}
      function to_auth(){{
        window.location.href="https://open.feishu.cn/open-apis/authen/v1/authorize?app_id={app_id}&redirect_uri="+get_redirect_url()+"&scope={scope}&state={app_id}"
      }}
      window.onload = function() {{
          document.querySelector('#url').textContent = get_redirect_url()
          document.getElementById('jumpButton').addEventListener('click', function() {{
             window.location.href = "https://open.feishu.cn/open-apis/authen/v1/authorize?app_id={app_id}&redirect_uri="+get_redirect_url()+"&scope={scope}&state={app_id}";
          }});
      }};
  </script>
</head>
<body>
    <p>第一步,飞书后台增加回调地址为:<span id="url"></span></p>
    <p>第二步,点击下方按钮,完成授权</p>
    <p><button id="jumpButton">授权</button></p>
</body>
</html>'''
            return 200, "text/html; charset=utf-8", html

        guide_url = WebhookUtils.add_webhook(self, "guide", ["GET"], guide, self.related_sync_system + "_guide")
        return {"action": "openwindow", "params": {"url": guide_url}}

    @staticmethod
    def get_description() -> dict:
        return {
            "name": "飞书",
            "type": "FEISHU",
            "params": [
                {
                    "name": "appId",
                    "key": "app_id",
                    "remark": "每个自建应用都拥有自己的App ID,创建应用后在凭证和基础信息中查看",
                    "required": True,
                    "type": "input"
                },
                {
                    "name": "appSecret",
                    "key": "app_secret",
                    "remark": "每个自建应用都拥有自己的App Secret,创建应用后在凭证和基础信息中查看",
                    "required": True,
                    "type": "input"
                }
            ]
        }

    @decode_request
    def _get_app_access_token(self):
        data = {
            'app_id': self.app_id,
            'app_secret': self.app_secret
        }
        return requests.post(
            f'https://open.feishu.cn/open-apis/auth/v3/app_access_token/internal',
            json=data,
            headers=self.headers
        )

    def get_app_access_token(self):
        app_access_token = SettingUtils.get_setting(self, "app_access_token", None)
        if app_access_token:
            self.app_access_token = app_access_token
            return app_access_token
        data = self._get_app_access_token()
        if data.get("code") != 0:
            raise ValueError(f"获取访问令牌失败:{data.get('msg')},请检查 app_id 或 app_secret 是否正确。")
        appToken = data.get("app_access_token")
        appExpire = data.get("expire")
        SettingUtils.set_setting(self, "app_access_token", appToken, expire=appExpire)
        return appToken

    @decode_request
    def _get_user_access_token(self, code, app_access_token=None):
        # 构建请求头
        headers = {
            'Authorization': f'Bearer {app_access_token if app_access_token else self.get_app_access_token()}',
            **self.headers  # 合并自定义头部
        }
        data = {
            'code': code,
            'grant_type': 'authorization_code'
        }
        return requests.post(
            f'https://open.feishu.cn/open-apis/authen/v1/oidc/access_token',
            json=data,
            headers=headers
        )

    def get_user_access_token(self):
        user_access_token = SettingUtils.get_setting(self, "user_access_token", None)
        if user_access_token:
            return user_access_token
        refresh_token = SettingUtils.get_setting(self, "refresh_token", None)
        assert refresh_token, "refresh_token not exists,need permission"
        data = self._refresh_token(refresh_token)
        userToken = data.get("access_token")
        userExpire = data.get("expires_in")
        refreshToken = data.get("refresh_token")
        refreshExpire = data.get("refresh_expires_in")
        SettingUtils.set_setting(self, "user_access_token", userToken, expire=userExpire)
        SettingUtils.set_setting(self, "refresh_token", refreshToken, expire=refreshExpire)
        return userToken

    @decode_request
    def _refresh_token(self, refresh_token):
        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_app_access_token()}',
            **self.headers  # 合并自定义头部
        }
        data = {
            'refresh_token': refresh_token,
            'grant_type': 'refresh_token'
        }
        return requests.post(
            f'https://open.feishu.cn/open-apis/authen/v1/oidc/refresh_access_token',
            json=data,
            headers=headers
        )

    @decode_request
    def get_spaces(self, page_token=None):

        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        params = {
            'lang': 'zh'
        }

        if page_token:
            params['page_token'] = page_token

        return requests.get(
            f'https://open.feishu.cn/open-apis/wiki/v2/spaces',
            params=params,
            headers=headers
        )

    @decode_request
    def get_nodes(self, spaceId, node_token=None, page_token=None):

        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        params = {}
        if node_token is not None:
            params['parent_node_token'] = node_token
        if page_token is not None:
            params['page_token'] = page_token

        if params:
            return requests.get(
                f'https://open.feishu.cn/open-apis/wiki/v2/spaces/{spaceId}/nodes',
                params=params,
                headers=headers
            )
        else:
            return requests.get(
                f'https://open.feishu.cn/open-apis/wiki/v2/spaces/{spaceId}/nodes',
                headers=headers
            )

    @decode_request
    def get_information_by_token(self, token):

        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        params = {
            'token': token
        }

        return requests.get(
            f'https://open.feishu.cn/open-apis/wiki/v2/spaces/get_node',
            params=params,
            headers=headers
        )

    @decode_request
    def get_information_by_id(self, user_id):

        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        return requests.get(
            f'https://open.feishu.cn/open-apis/contact/v3/users/{user_id}',
            headers=headers
        )

    @decode_request
    def get_file_information_by_token(self, node_token, obj_type):

        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        data = {
            "request_docs": [
                {
                    "doc_token": node_token,
                    "doc_type": obj_type
                }
            ],
            "with_url": "false"
        }

        return requests.post(
            f'https://open.feishu.cn/open-apis/drive/v1/metas/batch_query',
            json=data,
            headers=headers
        )


    @decode_request
    def create_export_task(self, obj_id, obj_type, file_extension):
        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        data = {
            'token': obj_id,
            'type': obj_type,
            'file_extension': file_extension
        }
        return requests.post(
            f'https://open.feishu.cn/open-apis/drive/v1/export_tasks',
            json=data,
            headers=headers
        )

    @decode_request
    def select_task_by_token(self, obj_token, ticket):

        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        params = {
            'token': obj_token
        }

        return requests.get(
            f'https://open.feishu.cn/open-apis/drive/v1/export_tasks/{ticket}',
            params=params,
            headers=headers
        )

    def download_task(self, fileToken):

        # 构建请求头
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        response = requests.get(
            f'https://open.feishu.cn/open-apis/drive/v1/export_tasks/file/{fileToken}/download',
            headers=headers
        )

        if response.status_code != 200:
            raise Exception(f"请求失败: {response.text}")
        return response

    @decode_request
    def get_files_list(self, page_token=None, folder_token=None):

        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }

        params = {}
        if page_token is not None:
            params['page_token'] = page_token
        if folder_token is not None:
            params['folder_token'] = folder_token

        if params:
            return requests.get(
                f'https://open.feishu.cn/open-apis/drive/v1/files',
                params=params,
                headers=headers
            )
        else:
            return requests.get(
                f'https://open.feishu.cn/open-apis/drive/v1/files',
                headers=headers
            )

    @decode_request
    def _search_file(self, query: str, file_type: str = None):

        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        data = {"search_key": query, "count": 50}
        if file_type:
            data["docs_types"] = [file_type]
        return requests.post("https://open.feishu.cn/open-apis/suite/docs-api/search/object", headers=headers,
                             json=data)

    @decode_request
    def _search_wiki(self, query: str, file_type: str = None):
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        data = {"query": query}
        param = {"page_size": 50}
        return requests.post("https://open.feishu.cn/open-apis/wiki/v1/nodes/search", headers=headers, json=data,
                             params=param)

    def search_file(self, query: str, file_type: str = None):
        wiki_files = self._search_wiki(query, file_type)
        wiki_files_filtered = [x for x in wiki_files["items"] if x["obj_type"] != "slides"]
        files = [{
            "id": f"{x['node_id']}_{x['obj_type']}_{x['obj_token']}",
            "name": x["title"],
            "type": "wiki",
            "is_file": True
        } for x in wiki_files_filtered]
        pan_files = self._search_file(query, file_type)
        an_files_filtered = [x for x in pan_files["docs_entities"] if x["docs_type"] != "slides"]
        files.extend([{
            "id": f"{x['docs_token']}_{x['docs_type']}",
            "name": x["title"],
            "type": "cloud_document",
            "is_file": True
        } for x in an_files_filtered])
        return files

    @decode_request
    def _get_space(self, **kwargs):
        """
        知识库空间
        """
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        return requests.get("https://open.feishu.cn/open-apis/wiki/v2/spaces", headers=headers, params=kwargs)

    def get_space(self, page_token=None, page_size: int = 10, lang: str = "zh"):
        """
        知识库空间
        """
        items = self._get_space(page_token=page_token, page_size=page_size, lang=lang)
        return {"files": [{
            "id": x['space_id'],
            "type": f"space_{x['space_id']}_",
            "is_file": False,
            "name": x["name"]
        } for x in items["items"]], "next_page_token": items["page_token"] if items['has_more'] else None}

    @decode_request
    def _get_space_file_list(self, space_id, **kwargs):
        """
        知识库空间文件
        """
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        return requests.get(f"https://open.feishu.cn/open-apis/wiki/v2/spaces/{space_id}/nodes", params=kwargs,
                            headers=headers)

    def get_space_file_list(self, space_id, page_token=None, page_size: int = 10, parent_node_token: str = None):
        """
        知识库空间文件
        """
        items = self._get_space_file_list(space_id, page_token=page_token, page_size=page_size,
                                          parent_node_token=parent_node_token)
        if "items" not in items:
            return {"files": [], "next_page_token": None}

        filtered_items = [x for x in items['items'] if x['obj_type'] != 'slides']

        return {"files": [{
            "id": f"{x['node_token']}_{x['obj_type']}_{x['obj_token']}",
            "type": f"space_{space_id}_{x['node_token']}",
            "is_file": True,
            "name": x["title"]
        }  for x in filtered_items], "next_page_token": items["page_token"] if items['has_more'] else None}

    @decode_request
    def _get_document_list(self, **kwargs):
        """
        文档
        """
        headers = {
            'Authorization': f'Bearer {self.get_user_access_token()}',
            **self.headers  # 合并自定义头部
        }
        return requests.get("https://open.feishu.cn/open-apis/drive/v1/files", headers=headers, params=kwargs)

    def get_document_list(self, folder_token=None, page_token=None, page_size: int = 10):
        items = self._get_document_list(page_token=page_token, page_size=page_size, folder_token=folder_token)

        filtered_items = [x for x in items['files'] if x['type'] != 'slides']
        return {"files": [{
            "id": f"{x['token']}_{x['type']}" if x['type'] != 'folder' else x['token'],
            "type": f"document_{x['token']}",
            "is_file": True if x['type'] != 'folder' else False,
            "name": x["name"]
        } for x in filtered_items], "next_page_token": items["next_page_token"] if items['has_more'] else None}

    def get_as_tree_node(self, file_id: str = None, file_type: str = None, next_page_token: str = None,
                         page_size: int = 20):
        if file_id is None and file_type is None:
            return {"files": [
                {"id": "wiki", "type": "wiki", "name": "知识库", "is_file": False},
                {"id": "document_", "type": "document_", "name": "云文档", "is_file": False}
            ], "next_page_token": None
            }

        if file_type == "wiki":
            return self.get_space(page_token=next_page_token, page_size=page_size)
        if file_type.startswith("space"):
            return self.get_space_file_list(file_type.split("_")[1], page_token=next_page_token, page_size=page_size,
                                            parent_node_token=file_type.split("_")[2])
        if file_type.startswith("document"):
            return self.get_document_list(folder_token=file_type.split("_")[1], page_token=next_page_token,
                                          page_size=page_size)
        return {
            "files": [], "next_page_token": None
        }
        return {
            "files": [], "next_page_token": None
        }


if __name__ == '__main__':
    from km_sdk.test_utils.cache_setting_test import reg_setting_cache_test

    reg_setting_cache_test()
    feishu_api = FeiShuApi(app_id="cli_a7848a6a40789013", app_secret="GvsAze5Wy6krRx1xh8E42bpVLCOWnVbM")
    print(feishu_api.get_as_tree_node())
    print(feishu_api.get_as_tree_node("", "wiki"))
    print(feishu_api.get_as_tree_node("", "space_7425931389272899585_"))
    print(feishu_api.get_as_tree_node("", "space_7426964309193621508_"))
    print(feishu_api.get_as_tree_node("KS0twMvOsivEdBku9nqc2cbBnaf_GdHNdnzUKoaRBsxuAeocjXyonSg_docx",
                                      "space_7426964309193621508_KS0twMvOsivEdBku9nqc2cbBnaf"))
    print(feishu_api.get_as_tree_node("PuojwL52NiPW03kgvKDcMqaLnah_MGKLdTtExojgAVxJbn5cNGR4nJc_docx",
                                      "space_7425931389272899585_PuojwL52NiPW03kgvKDcMqaLnah"))

    print(feishu_api.get_as_tree_node("T8UZfqhLsltp7ndWb98cQRiunLe", "document_Ud7qdtLHXoD2pXxwX1RcjZPKngb"))
