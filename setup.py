from setuptools import setup

setup(
    name="concat-pdf",
    version=0.1,
    author="Ritchie Vink",
    license='MIT License',
    packages=["concatPDF"],
    install_requires=[
        "PyPDF2==1.26.0"
    ]
)