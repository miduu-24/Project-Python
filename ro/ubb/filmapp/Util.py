def cnp(text: str = " "):
    """
    Function to verify if a CNP is valid
    :param text: message to print on input
    :return: int
    """
    try:
        x = int(input(text))
        y = str(x)
        if len(y) == 1:
            return x
        else:
            print('You forget some numbers. Try again.')
            return cnp(text)
    except ValueError:
        print("Your cnp must have just int numbers")
        return cnp(text)


def read_int(text: str = " "):
    """
    Function to read an integer from the terminal
    :param text: message to print on input
    :return: int
    """
    try:
        return int(input(text))
    except ValueError:
        print("\n Try again with an int \n")
        return read_int(text)