from setuptools import setup, find_packages

setup(
    name="torinmypackage",
    version="0.1",
    packages=find_packages(),
    description="Пример пакета с генераторами, итераторами, декораторами и дескрипторами",
    author="Torin",
    author_email="219mons@gmail.com",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
