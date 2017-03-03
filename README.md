# concatPDF

Simply concat PDF files based on their file names and configuration file.

The order is first based on the globbing in the config.ini file and second on the numerical order of the file names.

File names must start with a number, or an exception is thrown.

Valid names are:

* 1.0_my_nr_1pdf.pdf
* 4.pdf
* 3.13_the_third.PDF
* 1.1-i-will-be-second.pdf

## Concatenation order

Leading in determining the concatenation order is the `config.ini` file.

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

1. The configuration file above will first concatenate all pdf files matching the '1' glob in the `source/` directory.
2. Secondly all files in the `source/appendix/` directory are appended to the pdf.
3. And finally the remaining files in the `source/` directory are added.

Note that only pdf files will be added. So `*` can be safely used.

## Installation

`$ pip install git+https://github.com/ritchie46/concatPDF.git`

## Initialise a project

Go to you project directory and run:

`$ concatPDF`

To start the build run `make.py` from your projects root directory.

