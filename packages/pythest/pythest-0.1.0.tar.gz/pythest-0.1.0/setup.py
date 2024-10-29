from setuptools import setup, find_packages

setup(
    name="pythest",  # Nom de ton package
    version="0.1.0",  # Numéro de version
    author="Ton Nom",
    author_email="ton.email@example.com",
    description="Bonjour",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/bemaudettest/pythest",  # URL vers ton repo GitHub, par exemple
    packages=find_packages(),  # Trouve automatiquement tous les sous-modules
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Version minimale de Python
)