import unittest
from unittest.mock import patch
from decorators import devide

class TestDecorator(unittest.TestCase):
    def test_devide(self):
        # result=devide(3,2)
        # self.assertGreaterEqual(result,1)
        self.assertRaises(Exception, devide , 3,0)

if __name__ == '__main__':
    unittest.main()
