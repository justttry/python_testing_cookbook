# encoding: UTF-8

from widget import Widget
import unittest


########################################################################
class WidgetTestCase(unittest.TestCase):
    """"""

    #----------------------------------------------------------------------
    def setUp(self):
        """"""
        self.widget = Widget()
        
    #----------------------------------------------------------------------
    def tearDown(self):
        """"""
        self.widget.dispose()
        self.widget = None
        
    #----------------------------------------------------------------------
    def testSize(self):
        """"""
        self.assertEqual(self.widget.getSize(), (40, 40))
        
    #----------------------------------------------------------------------
    def testResize(self):
        """"""
        self.widget.resize(100, 100)
        self.assertEqual(self.widget.getSize(), (100, 100))
        

########################################################################
class WidgetTestSuite(unittest.TestSuite):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        unittest.TestSuite.__init__(self, map(WidgetTestCase,
                                              ("testSize",
                                               "testResize")))
        
        
def suite():
    suite = unittest.TestSuite()
    suite.addTest(WidgetTestCase('testSize'))
    suite.addTest(WidgetTestCase('testResize'))
    return suite


if __name__ == "__main__":
    #unittest.main(defaultTest = 'suite')
    
    #suite = suite()
    #runner = unittest.TextTestRunner()
    #runner.run(suite)
    unittest.main()