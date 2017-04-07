from setuptools import setup
import sys

if sys.version_info[0] != 3:
    sys.exit('Sorry, Python 2 is not supported')

try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except(IOError, ImportError):
    long_description = open('README.md').read()

setup(
    name="concatPDF",
    version="0.1.3",
    author="Ritchie Vink",
    license='MIT License',
    url="https://ritchievink.com",
    download_url="https://github.com/ritchie46/concatPDF",
    entry_points={
        'console_scripts': ['concatPDF=concatPDF.quickstart:run'],
    },
    packages=["concatPDF", "concatPDF/res"],
    install_requires=[
        "PyPDF2>=1.26.0"
    ],
    long_description=long_description,
    description="Merge PDF files just like a build process."
)