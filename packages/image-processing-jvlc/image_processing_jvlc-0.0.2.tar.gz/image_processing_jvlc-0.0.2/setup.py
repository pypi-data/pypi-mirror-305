from setuptools import setup, find_packages

with open("README.md", "r") as file:
    page_description = file.read()

with open("requirements.txt") as file:
    requirements = file.read().splitlines()

setup(
    name="image_processing_jvlc",
    version="0.0.2",
    author="João Leal",
    description="Image Processing Package using Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joaoVitorLeal/image-processing-package",
    packages=find_packages(),
    install_requires=requirements,
    python_requires=">=3.5"
)