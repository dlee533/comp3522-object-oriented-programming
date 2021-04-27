"""
(5 Marks)
TODO Define a function called convert_to_string(integer_sequence) that takes a sequence of integers as its parameter.
Define this function according to the requirements below:
•	Each number in the sequence should be an ASCII code for a corresponding character.
•	This function returns a string.
•	The function should use list comprehension(s) to convert the integer sequence to the string that is represented when all the numbers are converted to their corresponding ASCII character.

HINTS
•	chr(i) converts an integer to a character.
•	Numbers in the range 0 - 255 (inclusive) represent the ASCII character set.
"""


def convert_to_string(integer_sequence):
    str_list = [chr(num) for num in integer_sequence]
    separator = ""
    return separator.join(str_list)


# TODO run the program and achieve the expected output: Hello World
print(convert_to_string([72, 101, 108, 108, 111, 32, 87, 111, 114, 108, 100]))  # DON'T MODIFY THIS LINE
