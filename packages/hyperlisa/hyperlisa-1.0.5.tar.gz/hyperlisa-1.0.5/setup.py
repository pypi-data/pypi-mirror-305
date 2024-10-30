import os
import shutil
from setuptools import setup, find_packages

setup(
    name="hyperlisa",
    version="1.0.5",
    description="A package for combining source code files into one",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Omar Venturi",
    author_email="omar.venturi@hypertrue.com",
    url="https://github.com/moonClimber/hyperlisa",  # URL del repository GitHub
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "combine-code=lisa._combine_code:main",  # Comando originale
            "cmb=lisa._combine_code:main",  # Alias breve
            "lisacmb=lisa._combine_code:main",  # Alias descrittivo
            "hyperlisacmb=lisa._combine_code:main",  # Alias ancora più descrittivo
            "hyperlisa-configure=lisa.configure:main",  # Comando per configurazione manuale
        ],
    },
)
