from setuptools import setup, find_packages

setup(
    name='lerxmlspy',                      
    version='0.0.1',
    description='Um pacote para leitura de arquivos XML e converter para DataFrames',
    author='Rodrigo Schilling',
    packages=find_packages(),           
    install_requires=[
        'xmltodict',
        'pandas',
        'lxml'
    ],
)