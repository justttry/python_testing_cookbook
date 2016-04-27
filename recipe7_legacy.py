# encoding: UTF-8

from recipe7 import *


########################################################################
class RomanNumeralTester(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        self.cvt = RomanNumeralConverter()
        
    
    #----------------------------------------------------------------------
    def simple_test(self):
        """"""
        print '+++ converting M to 1000'
        assert self.cvt.convert_to_decimal('M') == 1000
        
    #----------------------------------------------------------------------
    def combo_test1(self):
        """"""
        print '+++ converting MMX to 2010'
        assert self.cvt.convert_to_decimal('MMX') == 2010
        
    #----------------------------------------------------------------------
    def combo_test2(self):
        """"""
        print '+++ converting MMMMDCLXVIII to 4668'
        val = self.cvt.convert_to_decimal('MMMMDCLXVIII')
        self.check(val, 4668)
        
    #----------------------------------------------------------------------
    def other_test(self):
        """"""
        print '+++ converting MMMM to 4000'
        val = self.cvt.convert_to_decimal('MMMM')
        self.check(val, 4000)
        
    #----------------------------------------------------------------------
    def check(self, actual, expected):
        """"""
        if actual != expected: 
            raise AssertionError("%s doesn't equal %s" %\
                                 (actual, expected))
    
    #----------------------------------------------------------------------
    def test_the_system(self):
        """"""
        self.simple_test()
        self.combo_test1()
        self.combo_test2()
        self.other_test()
    

if __name__ == '__main__':
    tester = RomanNumeralTester()
    tester.test_the_system()
    