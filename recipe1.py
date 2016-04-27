# encoding:UTF-8


########################################################################
class RomanNumeralConverter(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.digit_map =  {"m":1000, 'd':500, 'c':100, 'l':50,
                           'x':10, 'v':5, 'i':1}
        
    #----------------------------------------------------------------------
    def convert_to_decimal(self, roman_numeral):
        """"""
        val = 0
        for char in roman_numeral:
            val += self.digit_map[char]
        return val
        
        
    
    