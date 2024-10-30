from setuptools import setup
from setuptools import find_packages

with open("README.md", "r") as fh:
    long_desc = fh.read()

setup(
    name="valclient-remake", # Replace with your own username
    version="2.28",
    author="colinh",
    description="Wrapper for VALORANT's client API",
    long_description=long_desc,
    long_description_content_type="text/markdown",
    url="https://github.com/mbok1200/valclient-2.28",
    project_urls={},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.0",
)