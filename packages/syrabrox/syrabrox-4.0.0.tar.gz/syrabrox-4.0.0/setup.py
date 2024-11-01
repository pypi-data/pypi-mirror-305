from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    description = f.read()

setup(
    name="syrabrox",
    version="4.0.0",
    packages=find_packages(),
    install_requires=[
        # "numpy>=1.11.1"
    ],
    long_description=description,
    long_description_content_type="text/markdown"
)