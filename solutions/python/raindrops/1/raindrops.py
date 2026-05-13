"""This function converts the number and provide a corresponding raindrop sound based on the divisibility of the number"""

def convert(number):
    """
    This function converts the number to a corresponding raindrop sound based on the following:
    is divisible by 3, add "Pling" to the result.
    is divisible by 5, add "Plang" to the result.
    is divisible by 7, add "Plong" to the result.
    is not divisible by 3, 5, or 7, the result should be the number as a string.

    :param number: int - the number to be converted
    :result: int - a string value representing the raindrop sound
    """
    result = ''
    
    if number % 3 == 0:
        result = 'Pling'
        if number % 5 == 0 and number % 7 == 0:
            result = 'PlingPlangPlong'
        elif number % 7 == 0:
            result = 'PlingPlong'
        elif number % 5 == 0:
            result = 'PlingPlang'
                
    elif number % 5 == 0:
        result = 'Plang'
        if number % 7 == 0:
            result = 'PlangPlong'
            
    elif number % 7 == 0:
        result = 'Plong'
        
    else:
        result = str(number)    
    
    return result
