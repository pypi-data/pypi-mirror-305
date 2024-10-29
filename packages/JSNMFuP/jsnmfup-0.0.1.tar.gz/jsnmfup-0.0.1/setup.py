import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="JSNMFuP",# Replace with your own username
    version="0.0.1",
    author="Bai Zhang",
    author_email="942761959@qq.com",
    description="A unsupervised method for the integrative analysis of single-cell multi-omics data based on non-negative matrix factorization.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ZB-JN/JSNMFuP",
    packages=setuptools.find_packages(),
    py_modules=['JSNMFuP.model', 'JSNMFuP.utils'],  # 添加多个模块
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
