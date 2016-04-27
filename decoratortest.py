# encoding: UTF-8


#----------------------------------------------------------------------
def check_is_admin(f):
    """"""
    def wrapper(*args, **kwargs):
        print args
        print kwargs
        print kwargs.get('username')
        l = f(*args, **kwargs)
        return l
    return wrapper


########################################################################
class Store(object):
    """"""
    #----------------------------------------------------------------------
    def __init__(self):
        """"""
        self.storage = []

    #----------------------------------------------------------------------
    @check_is_admin
    def get_food(self, username, food):
        """"""
        return self.storage.get(food)
        
    #----------------------------------------------------------------------
    @check_is_admin
    def put_food(self, username, food):
        """"""
        print 'put food'
        self.storage.append(food)
    

test = Store() 
test.put_food('admin', 'rice')