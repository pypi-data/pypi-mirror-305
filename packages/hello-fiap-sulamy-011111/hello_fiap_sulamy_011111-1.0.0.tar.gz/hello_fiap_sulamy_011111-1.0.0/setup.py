from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='hello-fiap-sulamy-011111',
    version='1.0.0',
    packages=find_packages(),
    description='Uma biblioteca para demonstrar como subir no pypi',
    author='Renato morais',
    author_email='tadriano.dev@teste.com',
    url='',  
    license='MIT',  
    long_description=long_description,
    long_description_content_type='text/markdown' 
)