"This function calculate whether the given year is a leap year."

def leap_year(year):
    """
    Returns a boolean (True or False) if the given year is a leap year or not.

    :param year: int - the year to be determined if a leap year
    :return: bool - returns true if the given year is a leap year and false if not.
    """
    year_4 = year % 4 == 0
    year_100 = year % 100 == 0
    year_400 = year % 400 == 0
    
    return year_4 and (not year_100 or year_400)


    