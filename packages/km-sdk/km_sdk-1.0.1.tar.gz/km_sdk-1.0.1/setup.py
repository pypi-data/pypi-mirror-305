from setuptools import setup, find_packages
from km_sdk.cons import SDK_VERSION
setup(name='km_sdk',
      version=SDK_VERSION,
      install_requires=[
          'elasticsearch==8.12.1',
          'elasticsearch-dsl==8.12.0',
          'APScheduler==3.10.4',
          'StrEnum==0.4.15'
      ],
      packages=find_packages(),
      description='知识管理系统插件开发SDK',
      long_description="",
      license="",
      url="",

      author='KnowledgeManagement',
      include_package_data=True
      )
