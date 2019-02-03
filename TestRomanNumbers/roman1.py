roman_numeral_map = (('M', 1000),
('CM', 900),
('D', 500),
('CD', 400),
('C', 100),
('XC', 90),
('L', 50),
('XL', 40),
('X', 10),
('IX', 9),
('V', 5),
('IV', 4),
('I', 1))


def to_roman(n):
    """
    Convert an integer to a Roman number.
    """
    if n > 3999:
        raise OutOfRangeError("The number must be less than 4000")
        
    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            # The next line prints out each step of the translation:
            print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
    return result


class OutOfRangeError(ValueError):
    pass
