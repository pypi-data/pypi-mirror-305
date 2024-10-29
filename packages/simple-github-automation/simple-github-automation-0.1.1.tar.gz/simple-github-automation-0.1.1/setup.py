from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="simple-github-automation",
    version="0.1.1",
    author="Vikranth Udandarao",
    author_email="vikranth22570@iiitd.ac.in",
    description="A Python package for automating GitHub tasks.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Vikranth3140/simple-github-automation",
packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
