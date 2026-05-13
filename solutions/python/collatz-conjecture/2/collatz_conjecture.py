def steps(number):
    """
    This function takes in a positive integer, return the number of steps it takes to          reach 1 according to the rules of the Collatz Conjecture.

    :param number: int - a positive integer.
    :return: int - number of steps it took to reach 1.
    """
    if number <= 0:
        # example when argument is zero or a negative integer
        raise ValueError("Only positive integers are allowed")
        
    count = 0
    while number > 1:
        if number % 2 == 0:
            number = number / 2
        else:
            number = (number * 3) + 1
        count += 1
    return count
