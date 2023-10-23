from config import transitions, alphabet
from logger import Logger


class Machine:
    def __init__(self, logger_dir: str):
        self.logger = Logger(logger_dir)

    def check_alphabet(self, input_string: str) -> bool:
        for char in input_string:
            if char not in alphabet:
                self.logger.error("Input string not in alphabet")
                return False
        return True

    def check_row(self, cols: str):
        if not self.check_alphabet(cols):
            return

        row: int = 0  # init row (S)
        for i in range(len(cols)):
            if transitions[row][int(cols[i]) - 1] == -1:
                self.logger.error(f"Error: the string does not belong to a finite state machine\n{cols}\n{'~' * i}^")
                return
            row = transitions[row][int(cols[i]) - 1]

        self.logger.write(f'Success, input string: [{cols}]')
