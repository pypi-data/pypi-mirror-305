import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
    name="fucker_zju",  # 模块名称
    version="1.8.5",  # 当前版本
    author="凯子哥",  # 作者
    author_email="1156537327@qq.com",  # 作者邮箱
    description="一个非常NB的包",  # 模块简介
    long_description=long_description,  # 模块详细介绍
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/wupeiqi/fucker",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    # 模块相关的元数据
    package_data={
        'fucker_zju': ['**/*'],  # 指定要包含的文件类型
        },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    entry_points={
        'console_scripts': [
            'fucker_zju=fucker_zju.task:test',
        ],
    },
    install_requires=[
        'pillow',
    ],
    python_requires='>=3',
)