from concatPDF import init
import os

order = {
    "1": "1*",
    "2": "calculations/*",
    "3": "*"
}

init(order=order)
os.mkdir("./source/calculations")