from setuptools import setup, find_packages

setup(
    name="PyProcTree",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List of dependencies, e.g., 'numpy', 'dgl', etc.
    ],
    author="Anonymous",
    description="A Python package for process discovery using GNNs.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/jaxels20/PyProcTree",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.12',
)
