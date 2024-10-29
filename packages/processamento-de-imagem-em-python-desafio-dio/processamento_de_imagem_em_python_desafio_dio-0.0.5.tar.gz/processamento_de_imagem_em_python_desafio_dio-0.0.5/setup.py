from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_de_imagem_em_python_desafio_dio",
    version="0.0.5",
    author="João Paulo",
    description="Image Processing Package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaodatapaulo/criando-um-pacote-de-processamento-de-imagem-com-python",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)