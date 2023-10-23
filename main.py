from machine import Machine

if __name__ == "__main__":
    string = "start!"
    machine: Machine = Machine("./logs/logs.txt")

    while string != "-1":
        string: str = input()
        machine.check_row(string)
        print("next")
