import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="NcatBot",
    version="1.0.8",  # 包版本号，便于维护版本
    author="吃点李子",  # 作者，可以写自己的姓名
    author_email="2793415379@qq.com",  # 作者联系方式，可写自己的邮箱地址
    description="基于NapCat开发的PythonSDK",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8', # 对python的最低版本要求
    install_requires=[
        "requests",
        "websocket-client",
        "colorama",
        "tqdm",
        "python-box",
        "PYyaml"
    ]
)