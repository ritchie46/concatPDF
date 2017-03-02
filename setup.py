from setuptools import setup

setup(
    name="concatPDF",
    version="0.1.1",
    author="Ritchie Vink",
    license='MIT License',
    entry_points={
        'console_scripts': ['concatPDF=concatPDF.quickstart:run'],
    },
    packages=["concatPDF", "concatPDF/res"],
    install_requires=[
        "PyPDF2>=1.26.0"
    ]
)