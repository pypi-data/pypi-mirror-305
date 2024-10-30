# -*- coding: utf-8 -*-
# @Time    : 2024/10/29 19:38
# @Author  : BXZDYG
# @Software: PyCharm
# @File    : setup
# @Comment :
import setuptools  # 导入setuptools打包工具

from fastapi_brocaster import __version__

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="fastapi-broadcaster",  # 用自己的名替换其中的YOUR_USERNAME_
    version=__version__,  # 包版本号，便于维护版本
    author="BXZDYG",  # 作者，可以写自己的姓名
    author_email="banxingzhedeyangguang@gmail.com",  # 作者联系方式，可写自己的邮箱地址
    description="websocket using for fastapi channels",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    license="MIT",
    url="https://github.com/YGuang233/fastapi-channels",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    install_requires=[
        'fastapi>=0.110.0',
        'broadcaster>=0.3.1',
        'fastapi_limiter<=0.1.6'
    ],
    classifiers=[
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',  # 对python的最低版本要求
)
