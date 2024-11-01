from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="rennips",
    version="0.2.0",
    author="Oh Jongjin",
    author_email="5jx2oh@gmail.com",
    description="A minimalist Python progress spinner for iterative processes",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Oh-JongJin/rennips",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=[],
    keywords="rennips, progress, spinner, terminal, cli, progress-bar",
)