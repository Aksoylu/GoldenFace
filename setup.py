from setuptools import setup, find_packages

setup(
    name='goldenface',
    version='0.1',
    packages=find_packages(where='Library Source'),  # Point to the source folder
    install_requires=[],
    package_dir={'': 'Library Source'},  # Specify the source folder
)
