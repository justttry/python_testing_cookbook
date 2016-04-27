# encoding: UTF-8


########################################################################
class Fruit(object):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, color = 'red', price = 0):
        """Constructor"""
        self.__color = color
        self.__price = price
    
    #----------------------------------------------------------------------
    def __getattribute__(self, name):
        """"""
        return object.__getattribute__(self, name)
    
    #----------------------------------------------------------------------
    def __setattr__(self, name, value):
        """"""
        self.__dict__[name] = value
        
    #----------------------------------------------------------------------
    def __getitem__(self, name):
        """"""
        return self.__dict__[name]
        

if __name__ == '__main__':
    fruit = Fruit('blue', 10)
    print fruit.__dict__.get('_Fruit__color')
    fruit.__dict__['_Fruit__price'] = 5
    print fruit.__dict__.get('_Fruit__price')