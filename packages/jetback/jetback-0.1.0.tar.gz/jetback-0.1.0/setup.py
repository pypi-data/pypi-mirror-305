from setuptools import setup, find_packages
import os

def read_requirements(file):
    with open(file) as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Read the README for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="jetback",
    version="0.1.0",
    author="Jetback",
    author_email="amine@jetback.dev",
    description="JetBack.Dev Deployment utilities for Python web frameworks", 
    long_description=long_description,
    long_description_content_type="text/markdown",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    install_requires=read_requirements('requirements/base.txt'),
    extras_require={
        'flask': read_requirements('requirements/flask.txt'),
        'fastapi': read_requirements('requirements/fastapi.txt'),
        'django': read_requirements('requirements/django.txt'),
    },
    classifiers=[
        "Development Status :: 4 - Beta", 
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: FastAPI",
        "Framework :: Flask",
        "License :: Other/Proprietary License",
    ],
    python_requires=">=3.7",
    project_urls={
        "Homepage": "https://jetback.dev",
    },
)