from setuptools import setup, find_packages

# 读取 README 文件作为 long_description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# 读取 requirements.txt 中的依赖项
with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="NANO-filter",  # 包名
    version="0.1.0",  # 版本号
    author="Tianyi Zhang",
    author_email="zhangtia24@mails.tsinghua.edu.cn",
    description="Nonlinear Bayesian Filtering with Natural Gradient Gaussian Approximation",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/TianyiMehdi/NANO-filter",  # GitHub仓库地址
    packages=find_packages(),  # 自动查找包
    install_requires=requirements,  # 安装依赖
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",  # 更改为你的许可证
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",  # Python版本要求
)
