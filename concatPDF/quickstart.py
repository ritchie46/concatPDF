import os
import configparser
import pkg_resources


def init(source="./source", build="./build", order=None, out_name="output"):
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
        "2": "content/*"
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

if __name__ == "__main__":
    init()