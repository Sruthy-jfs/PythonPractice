import unittest
import demo

class TestMain(unittest.TestCase):#its the standard format for testcase
    def test_do_stuff(self):
        num=10
        result=demo.sum(num)
        self.assertEqual(result,15)

    def test_error(self):
        test_param='sfdfggg'
        result=demo.sum(test_param)
        self.assertTrue(isinstance(result, ValueError))



    def test_error2(self):
        test_param=None
        str='please enter a number'
        result=demo.sum(test_param)
        self.assertEqual(result,str)

    def test_error3(self):
        test_param=''
        str='please enter a number'
        result=demo.sum(test_param)
        self.assertEqual(result,str)


if __name__ == '__main__':
    unittest.main()
#test1 = TestMain()
#print(test1.test_do_stuff())
