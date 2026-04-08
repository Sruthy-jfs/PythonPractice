import unittest
import RandNumGenerator


class TestRandNum(unittest.TestCase):
    def test_error1(self):
        guess=10
        correct=10
        value=RandNumGenerator.run_guess(guess,correct)
        self.assertTrue(value)


    def test_error2(self):
        guess=10
        correct=5
        value=RandNumGenerator.run_guess(guess,correct)
        self.assertFalse(value)

    def test_error3(self):
        guess=11
        correct=5
        value=RandNumGenerator.run_guess(guess,correct)
        self.assertFalse(value)

    def test_error4(self):
        guess = 'a'
        correct = 5
        value = RandNumGenerator.run_guess(guess, correct)
        self.assertFalse(value)



    if __name__=='__main__':
        unittest.main()