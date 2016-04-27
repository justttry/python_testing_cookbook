from Queue import Queue
import random
import threading
import thread
import time


########################################################################
class Producter(threading.Thread):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, t_name, queue):
        """Constructor"""
        super(Producter, self).__init__(name = t_name)
        self.data = queue
        self.thread_id = 0
        
    #----------------------------------------------------------------------
    def run(self):
        """"""
        self.thread_id = thread.get_ident()
        print 'producter thread id: %d\n' % self.thread_id
        #wingdbstub.debugger.SetDebugThreads({self.thread_id:1})
        for i in range(10):
            print '%s : %s is producting %d to the queue!\n' %(time.ctime(),
                                                               self.getName(),
                                                               i)
            self.data.put(i)
            time.sleep(random.randrange(10)/5)
    
        print '%s : %s finished!' %(time.ctime(), self.getName())
        
        
        
########################################################################
class Consumer(threading.Thread):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, t_name, queue):
        """Constructor"""
        super(Consumer, self).__init__(name = t_name)
        self.data = queue
        self.thread_id = 0
        
    #----------------------------------------------------------------------
    def run(self):
        """"""
        import wingdbstub
        self.thread_id = thread.get_ident()
        print 'Consumer thread id: %d\n' % self.thread_id
        wingdbstub.debugger.SetDebugThreads({self.thread_id:1})
        for i in range(10):
            #import wingdbstub  
            if i == 1:
                print 'Cus. i = %d' %(i)
            val = self.data.get()
            print '%s : %s is consuming. %d in the queue is consumed!\n' \
                  %(time.ctime(), self.getName(), val)
            time.sleep(random.randrange(10))
        print "%s : %s finished!" %(time.ctime(), self.getName())
        

########################################################################
class NoAction(threading.Thread):
    """"""

    #----------------------------------------------------------------------
    def __init__(self, t_name):
        """Constructor"""
        super(NoAction, self).__init__(name = t_name)
        self.thread_id = 0
        
    #----------------------------------------------------------------------
    def run(self):
        """"""
        self.thread_id = thread.get_ident()
        print 'NoAction thread id: %d\n' % self.thread_id
        #wingdbstub.debugger.SetDebugThreads({self.thread_id:0})
        for i in range(20):
            print "%s : %s is running!! time %d" %(time.ctime(), self.getName(), i)
            time.sleep(random.randrange(10))
        print "%s : %s finished!!" %(time.ctime(), self.getName())
    
        

#----------------------------------------------------------------------
def main():
    """"""
    queue = Queue()
    producter = Producter('Pro.', queue)
    consumer  = Consumer('Con.', queue)
    noAction = NoAction('NoA.')
    producter.start()
    consumer.start()
    noAction.start()
    producter.join()   
    consumer.join()
    noAction.join()
    
    print 'all threads terminate!'
    

if __name__ == '__main__':
    main()