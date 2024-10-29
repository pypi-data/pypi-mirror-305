from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="parquet-viewer",
    version="0.1.1",
    author="Ashutosh Bele",
    author_email="ashutoshbele5@gmail.com",
    description="A powerful command-line tool for viewing Parquet files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/parquet-viewer",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "pyarrow",
        # add other dependencies
    ],
    entry_points={
        "console_scripts": [
            "pqview=parquet_viewer.cli:main",
        ],
    },
) 