from setuptools import setup, find_packages

# Leer el contenido del archivo README.md
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="bad4u",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[],
    author="Badreflexz",
    description="Una biblioteca de skills",
    long_description=long_description,
    long_description_content_type="text/markdown",
)
