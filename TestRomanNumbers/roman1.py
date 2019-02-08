"""
Rules for Roman numbers:

• Sometimes characters are additive. I is 1, II is 2, and III is 3. VI is 6
(literally, “5 and 1”), VII is 7, and VIII is 8.

• The tens characters (I, X, C, and M) can be repeated up to three times. At 4,
you need to subtract from the next highest fives character. You can't represent
4 as IIII; instead, it is represented as IV (“1 less than 5”).

40 is written as XL (“10 less than 50”), 41 as XLI, 42 as XLII, 43 as XLIII, and then 44 as XLIV (“10 less than 50, then 1 less than 5”).

• Sometimes characters are… the opposite of additive. By putting certain
characters before others, you subtract from the final value. For example, at 9,
you need to subtract from the next highest tens character: 8 is VIII, but 9 is
IX (“1 less than 10”), not VIIII (since the I character can not be repeated
four times). 90 is XC, 900 is CM.

• The fives characters can not be repeated. 10 is always represented as X,
never as VV. 100 is always C, never LL.

• Roman numerals are read left to right, so the order of characters matters
very much. DC is 600; CD is accompletely different number (400, “100 less than
500”). CI is 101; IC is not even a valid Roman numeral (because you can't
subtract 1 directly from 100; you would need to write it as XCIX, “10 less than
100, then 1 less than 10”).
"""

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
    # Numbers can't be less than 1 or greater than 3999
    if not(0 < n < 4000):
        raise OutOfRangeError("The number must be positive and less than 4000")

    if not isinstance(n, int):
        raise NotIntegerError("Only whole numbers are allowed")

    result = ""
    for numeral, integer in roman_numeral_map:
        while n >= integer:
            result += numeral
            n -= integer
            # The next line prints out each step of the translation:
            print('subtracting {0} from input, adding {1} to output'.format(integer, numeral))
    return result

def from_roman():
    """
    Convert a string from a Roman numeral to an integer.
    """
    result = 0
    index = 0
    for numeral, integer in roman_numeral_map:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
            print('found', numeral, 'of length', len(numeral), ', adding', integer)
    return result


class InvalidRomanNumeralError(ValueError): pass
