from setuptools import setup

setup(
    name="concatPDF",
    version="0.1.0",
    author="Ritchie Vink",
    license='MIT License',
    packages=["concatPDF", "concatPDF/res"],
    install_requires=[
        "PyPDF2==1.26.0"
    ]
)