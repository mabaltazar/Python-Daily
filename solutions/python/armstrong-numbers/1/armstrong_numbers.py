"""This function determines if the given number is an armstrong number or not."""

def is_armstrong_number(number: int) -> bool:
    """
    This function takes in a positive integer value and determines if the number is an             armstrong number.
    :param:number: int - the number to be determined if armstrong or not
    :return: bool - returns True if number is an armstrong number and False if not.
    """
    
    nbr = abs(number) #convert number to positive integer
    digits = str(nbr) #convert number to string value
    nbr_count = len(digits) # count the number of digits
    
    total = sum(int(digit) ** nbr_count for digit in digits)
    
    return total == nbr
    