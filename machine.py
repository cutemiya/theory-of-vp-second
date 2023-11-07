from config import transitions, alphabet
from logger import Logger


class Machine:
    def __init__(self, logger_dir: str):
        self.logger = Logger(logger_dir)

    def check_alphabet(self, input_string: str) -> bool:
        for char in input_string:
            if char not in alphabet:
                self.logger.error("Error: input string not in alphabet")
                return False
        return True

    def check_empty(self, input_string: str) -> bool:
        if input_string == '' or not input_string:
            self.logger.error("Error: string is empty")
            return False
        return True

    def check_row(self, cols: str):
        if not self.check_alphabet(cols):
            return

        if not self.check_empty(cols):
            return

        row: int = 0  # init row (S)
        for i in range(len(cols)):
            if transitions[row][int(cols[i]) - 1] == -1:
                self.logger.error(f"Error: the string does not belong to a finite state machine\n{cols}\n{'~' * i}^")
                return
            row = transitions[row][int(cols[i]) - 1]

        if row == 4:
            self.logger.write(f'OK: Success, input string: [{cols}]')
        else:
            self.logger.error(f"Мы не дошли до конечного состояния, input string [{cols}]")
