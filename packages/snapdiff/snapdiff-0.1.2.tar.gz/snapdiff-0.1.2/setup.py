from setuptools import setup, find_packages
from pathlib import Path


with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()


setup(
    name="snapdiff",
    version="0.1.2",
    description="A package for comparing snapshots of data and tracking differences when function change",
    long_description=(Path(__file__).parent / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Ahmed Hendy",
    author_email="ahmedelsyd5@gmail.com",
    url="https://github.com/ahmedhendy/snapdiff",
    packages=find_packages(),
    install_requires=requirements,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    data_files=[("", ["requirements.txt"])],
    python_requires=">=3.7",
)
