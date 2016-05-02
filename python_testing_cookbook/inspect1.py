# encoding: UTF-8

import sys
import inspect


def foo():pass


########################################################################
class Cat(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, name = 'kitty'):
        """Constructor"""
        self.name = name
    
    
    #----------------------------------------------------------------------
    def sayHi(self):
        """"""
        print self.name, 'says Hi!'
        

#----------------------------------------------------------------------
def foo():
    """"""
    n = 1
    def bar():
        print n
    n = 2
    return bar