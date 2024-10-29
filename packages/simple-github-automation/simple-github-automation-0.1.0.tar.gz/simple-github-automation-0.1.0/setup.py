from setuptools import setup, find_packages

setup(
    name="simple-github-automation",
    version="0.1.0",
    author="Vikranth Udandarao",
    author_email="vikranth22570@iiitd.ac.in",
    description="A package for automating GitHub workflows",
    packages=find_packages("src"),
    package_dir={"": "src"},
    install_requires=["requests"],  # or add 'PyGithub' if you prefer
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
