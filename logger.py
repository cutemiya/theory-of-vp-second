import datetime
from typing import IO


class Logger:
    def __init__(self, directory: str):
        self.file: IO = open(directory, "a+", encoding='utf-8')

    def close_logger(self) -> None:
        self.file.close()

    def write(self, message: str) -> None:
        title: str = f"\n\n-----Okay----- time:[{datetime.datetime.now()}]:\n"
        self.file.write(title)
        self.file.write(message)

    def error(self, message: str) -> None:
        title: str = f"\n\n-----Error----- time:[{datetime.datetime.now()}]:\n"
        self.file.write(title)
        self.file.write(message)
