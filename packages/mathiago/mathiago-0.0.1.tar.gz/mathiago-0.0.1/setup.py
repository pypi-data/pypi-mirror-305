from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="mathiago",
    version="0.0.1",
    author="tavares_tiag",
    author_email="tiagoalvestavares1@gmail.com",
    description="Pacote com funções matemáticas para treino em python",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tavarestiag",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)