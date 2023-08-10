import logging

integer = 50
string = "The number is"

try:
    print(string + integer)
except TypeError as err:
    logging.warning(f"Error - {err}. You cannot add a string to an integer, without converting the integer to a string first.")
