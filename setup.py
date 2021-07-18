from setuptools import setup, find_packages

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='boitata-service',
    version='0.1.0',
    description='A service responsible to process and store data',
    long_description=readme,
    author='Thais Amorim',
    url='https://github.com/thasmarinho/boitata-service',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)