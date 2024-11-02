from setuptools import setup, find_packages

setup(
    name='lerxmlspy',                      
    version='0.0.2',
    description='Um pacote para leitura de arquivos XML e converter para DataFrames',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Rodrigo Schilling',
    author_email='rodrigo.schilling98@gmail.com',
    url='https://github.com/RoSchilling/lerxmlspy',
    packages=find_packages(),           
    install_requires=[
        'xmltodict',
        'pandas',
        'lxml'
    ],
)