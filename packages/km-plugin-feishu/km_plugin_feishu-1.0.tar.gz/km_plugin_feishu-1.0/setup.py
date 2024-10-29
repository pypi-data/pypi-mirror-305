import km_sdk.cons
from setuptools import setup, find_packages

setup(name='km-plugin-feishu',
      version='1.0',
      install_requires=[
          'km-sdk',
          'requests',
      ],
      dependency_links=[
          'https://pipy.cloudladder.net.cn/repository/km/simple',
      ],
      entry_points={
          km_sdk.cons.PLUGIN_GROUP_NAME: [
              'FEISHU = km_plugin_feishu.feishu_api:FeiShuApi'
          ]
      },
      packages=find_packages(),
      description='知识管理系统插件-飞书系统对接',
      author='KnowledgeManagement',
      )
