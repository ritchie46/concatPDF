import os
import pkg_resources


def init(source="./source", build="./build"):
    try:
        os.mkdir(build)
    except FileExistsError:
        pass
    try:
        os.mkdir(source)
    except FileExistsError:
        pass


    _replace = {
        b"{1}": bytes(build, "utf-8"),
        b"{2}": bytes(source, "utf-8")
    }

    res_pkg = __name__
    res_path = "/".join(("res", "config.ini"))
    s = pkg_resources.resource_string(res_pkg, res_path)
    for i, j in _replace.items():
        s = s.replace(i, j)

    with open("./config.ini", 'wb') as f:
        f.write(s)

if __name__ == "__main__":
    init()