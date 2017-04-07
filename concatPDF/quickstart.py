import os
import configparser
import pkg_resources
import argparse
from PyPDF2 import PdfFileReader, PdfFileWriter


def init(source="./source", build="./build", out_name="output", order=None):
    try:
        os.mkdir(build)
    except FileExistsError:
        pass
    try:
        os.mkdir(source)
    except FileExistsError:
        pass

    config = configparser.ConfigParser()
    config["DIR"] = {
        "build": build,
        "source": source
    }

    if order is None:
        order = {
        "1": "*",
        "2": "appendix/*"
    }

    config["ORDER"] = order
    config["OUTPUT"] = {
        "filename": out_name
    }

    with open("./config.ini", 'w') as f:
        config.write(f)

    # Makefile
    res_pkg = __name__
    res_path = "/".join(("res", "make.py"))
    s = pkg_resources.resource_string(res_pkg, res_path)

    with open("./make.py", 'wb') as f:
        f.write(s)


def split(fp):
    """
    Split PDF in one pagers.

    :param fp: (str) Path to PDF file to split.
    :return:
    """

    print("Splitting {} into multiple PDF files.".format(fp))
    with open(fp, "rb") as f:
        pdf = PdfFileReader(f)

        for i in range(pdf.numPages):
            print("Processing page {} of {}".format(i + 1, pdf.numPages))
            out = PdfFileWriter()
            out.addPage(pdf.getPage(i))
            with open("{}/{}._{}.pdf".format(os.path.dirname(fp), i + 1, os.path.basename(fp)[:-4]), "wb") as fw:
                out.write(fw)
        print("Finished")


def run():
    p = argparse.ArgumentParser()
    p.add_argument("--build", help="set build directory - standard: './build'")
    p.add_argument("--source", help="set source directory - standard: './source'")
    p.add_argument("--output", help="name of the output file - standard: 'output'")
    p.add_argument("--split", help="split file in one pagers")
    args = p.parse_args()

    if args.split:
        split(args.split)
    else:
        build = args.build if args.build else "./build"
        source = args.source if args.source else "./source"
        output = args.output if args.output else "./output"
        print("Preparing the build directories.\n\nThe build directory will be set to %s." % build,
              "\nThe source directory will be set to %s." % source,
              "\nThe output file will be merged as %s.pdf." % output)
        init(source, build, output)

if __name__ == "__main__":
    run()
