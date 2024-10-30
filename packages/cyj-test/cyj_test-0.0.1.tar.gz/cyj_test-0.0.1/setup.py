import platform
from setuptools import setup, find_packages

setup(
    name="cyj_test",  # 你的包名称
    version="0.0.1",  # 初始版本号
    description="A description of cyj package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="yinchenjue",
    author_email="454194347@qq.com",
    packages=find_packages(),
    install_requires=[],  # 如果有依赖包，在这里列出
    package_data={
        # 包含C动态库文件
        "cyj_test": ["libxugusql.so"] if platform.system() == "Linux" else ["xugusql.dll"],
    },
    python_requires=">=3.6",
)

