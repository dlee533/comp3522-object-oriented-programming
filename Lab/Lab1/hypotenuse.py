import math


def CalculateHypotenuse(a: float, b: float) -> float:
    """
    Return the hypotenuse of the right triangle given lengths of two sides as arguments.

    :param a: a float
    :param b: a float
    :precondition: a must be a float
    :precondition: b must be a float
    :return: square root of the sum of a and b to the power of two
    """
    return math.sqrt(a ** 2 + b ** 2)


def Sum(a: float, b: float) -> float:
    """
    Return the sum of two arguments.

    :param a: a float
    :param b: a float
    :precondition: a must be a float
    :precondition: b must be a float
    :return: sum of a and b
    """
    return a + b


def Multiply(a: float, b: float) -> float:
    """
    Return the product of two arguments.

    :param a: a float
    :param b: a float
    :precondition: a must be a float
    :precondition: b must be a float
    :return: product of a and b
    """
    return a * b


def Divide(a: float, b: float) -> float:
    """
    Return the divided result from the first argument by the second argument.

    :param a: a float
    :param b: a float
    :precondition: a must be a float
    :precondition: b must be a float
    :return: result of a divided by b
    """
    return a / b


def Subtract(a: float, b: float) -> float:
    """
    Return the subtracted result from the first argument by the second argument.

    :param a: a float
    :param b: a float
    :precondition: a must be a float
    :precondition: b must be a float
    :return: result of a subtracted by b
    """
    return a - b


def main():
    """
    Execute functions in the module.

    :param: none
    :precondition: none
    :return: none
    """
    operation = int(input("1 to calculate hypotenuse\n"
                          "2 to add\n"
                          "3 to subtract\n"
                          "4 to multiply\n"
                          "5 to divide\n"))
    if operation < 1 or operation > 5:
        print("invalid input")
        return
    first_num = float(input("enter first number: "))
    second_num = float(input("enter second number: "))
    if operation == 1:
        print(CalculateHypotenuse(first_num, second_num))
    elif operation == 2:
        print(Sum(first_num, second_num))
    elif operation == 3:
        print(Subtract(first_num, second_num))
    elif operation == 4:
        print(Multiply(first_num, second_num))
    else:
        print(Divide(first_num, second_num))


if __name__ == "__main__":
    main()