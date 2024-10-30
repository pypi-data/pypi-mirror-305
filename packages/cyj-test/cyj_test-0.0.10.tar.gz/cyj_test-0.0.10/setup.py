import platform
from setuptools import setup, find_packages
import sys

def get_python_version_string():
    # 获取 Python 版本的主和次版本号
    major = sys.version_info.major
    minor = sys.version_info.minor
    if major =='2':
        return "_pyxgdb.so"
    # 将主和次版本号转换为字符串格式
    version_string = f"{major}{minor}"
    return version_string

setup(
    name="cyj_test",  # 你的包名称
    version="0.0.10",  # 初始版本号
    description="A description of cyj package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="yinchenjue",
    author_email="454194347@qq.com",
    include_package_data=True,
    packages=find_packages(),
    install_requires=[],  # 如果有依赖包，在这里列出
    data_files=['cyj_test/python39/_pyxgdb.cpython-39-x86_64-linux-gnu.so'],
    package_data={
        # 包含C动态库文件
        #'cyj_test' : [f"*{get_python_version_string()}*"],
        #"cyj_test": ["libxugusql.so"] if platform.system() == "Linux" else ["xugusql.dll"],
    },
    python_requires=">=3.6",
)

