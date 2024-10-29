from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="parquet-viewer",
    version="0.1.3",
    author="Ashutosh Bele",
    author_email="ashutoshbele5@gmail.com",
    description="A powerful command-line tool for viewing Parquet files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Ashlo/ParquetViewer",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    install_requires=[
        "pandas",
        "pyarrow",
        "tabulate",
        "click"

    ],
    entry_points={
        "console_scripts": [
            "pqview=parquet_viewer.cli:main",
        ],
    },
) 