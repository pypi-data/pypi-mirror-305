from setuptools import setup, find_packages

setup(
    name="tinytroupe",
    version="0.0.1",
    description="This is a placeholder for the TinyTroupe library.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/microsoft/tinytroupe",  # Replace with the actual URL
    author="Paulo Salem",
    author_email="paulo.salem@microsoft.com",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.10",
    install_requires=[],
)