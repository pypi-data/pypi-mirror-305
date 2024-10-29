from setuptools import setup, find_packages
from pathlib import Path

# Read the contents of README.md
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name='TehilliDay',  # New package name
    version='0.1.0',
    description='A library to fetch daily Tehillim (Psalms)',
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify markdown for PyPI
    packages=find_packages(),
    install_requires=['requests'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
