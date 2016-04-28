# encoding: UTF-8

# there is something different here!

import math


#----------------------------------------------------------------------
def convert_to_basen(value, base):
    """Convert a base10 number to basen.edur
    >>> convert_to_basen(1, 2)
    '1'
    >>> convert_to_basen(2, 2)
    '10'
    >>> convert_to_basen(3, 2)
    '11'
    >>> convert_to_basen(4, 2)
    '100'
    >>> convert_to_basen(5, 2)
    '101'
    >>> convert_to_basen(6, 2)
    '110'
    >>> convert_to_basen(7, 2)
    '111'
    >>> convert_to_basen(1, 16)
    '1'
    >>> convert_to_basen(10, 16)
    'a'
    >>> convert_to_basen(15, 16)
    'f'
    >>> convert_to_basen(16, 16)
    '10'
    >>> convert_to_basen(31, 16)
    '1f'
    >>> convert_to_basen(32, 16)
    '20'
    """    
    def stringfy(value):
        if value >= 10:
            return chr(value + ord('a') - 10)
        else:
            return str(value)
    
    if value < base:
        return stringfy(value)
    else:
        return convert_to_basen(int(value / base), base) + stringfy(value % base)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
    
