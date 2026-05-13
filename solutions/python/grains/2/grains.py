""" 
The square(number) function calculates the number of grains in the specific square number.
The total() function calculates the total number of grains in the chessboard.
"""

def square(number):
    """
    This function calculates the number of grain in the given number from 1 to 64.
    
    :param number: int - number in the chessboard from 1 to 64
    :return: int - the number of grain in the given number
    """
    if number <= 0 or number > 64:
        raise ValueError("square must be between 1 and 64")
    for nbr in range(1, number+1):
        if nbr in [1,2]:
            sqr = nbr
        else:
            sqr += sqr
    return sqr

def total():
    """
    This function calculates the total number of grains in the chessboard.

    :return: int - returns the total number of grains in the chessboard.
    """
    for num in range(1, 65+1):
        if num in [1,2]:
            count = num
        else:
            count += count
    return count-1
        
