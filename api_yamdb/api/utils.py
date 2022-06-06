from random import randint


def get_confirmation_code() -> str:
    confirmation_code = ''
    for i in range(0, 6):
        i = str(randint(0, 9))
        confirmation_code += i
    return confirmation_code
