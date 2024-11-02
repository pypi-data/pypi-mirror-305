from setuptools import setup, find_packages

setup(name='km-plugin-ecm',
      version='1.2',
      install_requires=[
          'km-sdk>=1.0.1',
          'requests',
      ],
      dependency_links=[
          'https://pipy.cloudladder.net.cn/repository/km/simple',
      ],
      entry_points={
          "knowledge_management_plugin": [
              'ECM = km_plugin_ecm.ecm_api:EcmApi'
          ]
      },
      packages=find_packages(),
      description='知识管理系统插件-洪翼系统对接',
      author='KnowledgeManagement',
      )
