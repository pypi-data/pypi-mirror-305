from setuptools import setup, find_packages

setup(
    name="vgstools",
    version="0.1",
    packages=find_packages(include=["tools", "tools.*"]),
    install_requires=[],
    author="Enderz",
    description="A collection of the tools I made in my first year",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Enderz420/vgstools",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    license="MIT",
)
