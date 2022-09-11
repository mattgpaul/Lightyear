from setuptools import setup
from setuptools import find_packages

setup(
    name='Lightyear',
    version='0.0.1',
    author='Matthew Paul',
    author_email='mattgpaul@gmail.com',
    packages=find_packages(exclude=('tests*'))
)
