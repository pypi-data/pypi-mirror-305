# setup.py

from setuptools import setup, find_packages

setup(
    name="SAGE_core",
    version="0.0.1",
    description="Flexible plugin-based core library for extensible systems.",
    author="AGStudios",
    author_email="amckinatorgames@gmail.com",
    packages=find_packages(),
    install_requires=[],
    python_requires=">=3.6",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
