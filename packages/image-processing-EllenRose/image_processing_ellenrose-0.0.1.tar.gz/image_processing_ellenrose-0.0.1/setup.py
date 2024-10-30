from setuptools import setup, find_packages

# Ler a descrição longa do arquivo README.md
with open("README.md", "r") as f:
    page_description = f.read()

# Ler as dependências do arquivo requirements.txt
with open("requirements.txt", "r") as f:
    requirements = f.read().splitlines()

setup(
    name="image_processing_EllenRose",
    version="0.0.1",
    author="Ellen",
    author_email="ellenrvictoriano@gmail.com",
    description="Dio_Desafio_imagens_Python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EllenRose/image-processing-package.git",
    packages=find_packages(),
    install_requires=requirements,
)
