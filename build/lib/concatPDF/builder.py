from PyPDF2 import PdfFileMerger, PdfFileReader
import configparser
import os
import glob
import re
import string


def strtof(text):
    """
    Convect string to float.

    :param text: (str) String chunk
    :return: (list) ["foo, 12.1, "bar", 3.0]
    """
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
    return [strtof(c) for c in re.split('(^_\d+.\d+|\d+)', text) if c != '']


def progress_bar(progress):
    """
    Creates a simple progress bar.

    [#########_] 90%

    :param progress: (float) Percentage.
    """
    n = int(progress / 10)
    print('\r[{0}{1}] {2}%'.format('#' * n, '_' * (10 - n), progress), end='')


class Build:
    def __init__(self, config="./config.ini"):
        self.config = configparser.ConfigParser()
        self.config.read(config)
        self.source_dir = self.config["DIR"]["SOURCE"]
        self.build_dir = self.config["DIR"]["BUILD"]
        self.order = dict(self.config["ORDER"])
        self.output_name = self.config["OUTPUT"]["FILENAME"]
        self.paths = None

    def _def_path_order(self, extension=".pdf"):
        """
        Determine the concatenation order of the files.

        :param extension: (str) File extension.
        :return: (list) with path names.
        """
        files = []
        for i in range(1, len(self.order) + 1):
            _glob = self.order[str(i)]
            # Matching path names, unsorted.
            paths_us = glob.glob("%s/%s*%s" % (self.source_dir, _glob, extension))

            # Get the file names.
            ordered_fnames = []
            for f_path in paths_us:
                f = os.path.basename(f_path)
                # Files not starting with a digit are ignored.
                print(f)
                if f[0] in string.digits:
                    print("yes")
                    ordered_fnames.append(f)

            # Sort the file names
            ordered_fnames.sort(key=natural_keys)

            # File names are not complete paths, thus sort the paths also.
            # Sort the paths by the sorted filename list
            paths_s = []  # Matching path names, sorted.
            for f in ordered_fnames:
                for path_f in paths_us:
                    if f in path_f:
                        paths_s.append(path_f)
                        break
            # If query is new, append.
            for file_path in paths_s:
                if file_path not in files:
                    files.append(file_path)

        self.paths = files

    def concat(self, name):
        """
        Concatenate the pdf files found in _def_path_order().

        :param name: (str) Output file name.
        """
        merge = PdfFileMerger()
        n = len(self.paths)
        c = 0
        for f in self.paths:
            progress_bar(c / n * 100)
            with open(f, 'rb') as f:
                merge.append(PdfFileReader(f))
            c += 1
        merge.write(os.path.join(self.build_dir, "%s.pdf" % name))

    def build(self):
        """
        Build the out pdf.
        """

        self._def_path_order()
        if len(self.paths) == 0:
            print("\nNo pdf files found that meet the requirements. Have you numbered them?")
        else:
            print("\nBuilding pdf file in {0}/{1}.pdf".format(self.build_dir, self.output_name))
            self.concat(self.output_name)




