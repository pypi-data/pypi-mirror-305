from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='hello-fiap-sulamy-011111',
    version='1.0.1',
    packages=find_packages(),
    description='Uma biblioteca para demonstrar como subir no pypi',
    author='Sulamy morais',
    author_email='',
    url='',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown' 
)