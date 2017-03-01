import os
import configparser


def init(source="./source", build="./build", order=None):
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

    with open("./config.ini", 'w') as f:
        config.write(f)

if __name__ == "__main__":
    init()