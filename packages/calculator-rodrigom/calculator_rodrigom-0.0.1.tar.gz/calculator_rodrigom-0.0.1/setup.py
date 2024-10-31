from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

setup(
    name="calculator_rodrigom",
    version="0.0.1",
    author="Rodrigo M.",
    author_email="rodrigofmacarini@gmail.com",
    description="A calculator",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rodrigomacarini/python_language_fundamentals/tree/main/calculator",
    packages=find_packages(),
    python_requires='>=3.8',
)