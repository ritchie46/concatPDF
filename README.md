# concatPDF

Simply concat PDF files based on their file names and configuration file.

The order is first based on the globbing in the config.ini file and second on the numerical order of the file names.

File names must start with a number, or an exception is thrown.

Valid names are:

* 1_mypdf.pdf
* 4.pdf
* 3.13_thethird.PDF

## Concatenation order

Leading in determining the concatenation order is the config.ini file.

Example config.ini
```
    [DIR]
    build = ./build
    source = ./source

    [ORDER]
    1 = 1*
    2 = appendix/*
    3 = *

    [OUTPUT]
    filename = output
```

1. The configuration file above will first concatenate all pdf files matching the '1' glob in the 'source/' directory.
2. Secondly all files in the 'source/appendix/' directory are appended to the pdf.
3. And finally the remaining files in the 'source/' directory are added.

## Initialise a project

Following is an example of how you could initialise a project. Run from the project root directory:

```python
    from concatPDF import init
    import os

    order = {
        "1": "report/*",
        "2": "calculations/*",
        "3": "*"
    }

    init(order=order)
```

To start the build run `make.py` from your projects root.

## Installation

`$ pip install concatPDF`