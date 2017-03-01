from PyPDF2 import PdfFileMerger, PdfFileReader
import configparser
import os
import glob
import re

def strtof(text):
    """
    Convect string to float.
    :param text: (str) String chunk
    :return: (list) ["foo, 12.1, "bar", 3.0]
    """
    if text != '':
        try:
            return float(text) if text[0].isnumeric() else text
        except ValueError:
            return text


def natural_keys(text):
    """
    Query for floating number strings and turn them into floats.

    Function will be called by pythons sort method.
    :param (str)
    :return (list) With parameters to sort by.
    """
    return [strtof(c) for c in re.split('(\d.\d+|\d+)', text)]


class Build:
    def __init__(self, config="./config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config)
        self.source_dir = self.config["DIR"]["SOURCE"]
        self.build_dir = self.config["DIR"]["BUILD"]
        self.order = dict(self.config["ORDER"])
        self.paths = None

    def _def_path_order(self):
        files = []
        for i in range(1, len(self.order) + 1):
            _glob = self.order[str(i)]
            # Matching path names, unsorted.
            fs_us = glob.glob("%s/%s*.pdf" % (self.source_dir, _glob))

            # Get the file names.
            ordered_fnames = []
            for f in fs_us:
                ordered_fnames.append(os.path.basename(f))

            # Sort the file names
            ordered_fnames.sort(key=natural_keys)

            # Sort the paths by the sorted filename list
            fs_s = []  # Matching path names, sorted.
            for f in ordered_fnames:
                for path_f in fs_us:
                    if f in path_f:
                        fs_s.append(path_f)
                        break
            # If query is new, append.
            for f in fs_s:
                if f not in files:
                    files.append(f)
        self.paths = files

    def concat(self, name):
        merge = PdfFileMerger()
        for f in self.paths:
            with open(f, 'rb') as f:
                merge.append(PdfFileReader(f))

        merge.write(os.path.join(self.build_dir, "%s.pdf" % name))

    def build(self, name="output"):
        self._def_path_order()
        self.concat(name)





# merge = PdfFileMerger()

a = Build()
a._def_path_order()
a.concat()
