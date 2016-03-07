from my_module import my_module as nestedmodule
import unittest
from ddt import ddt, data

@ddt
class MyTestCase(unittest.TestCase):

    @data(3, 4, 10)
    def test_larger_than_two(self, number):
        self.assertTrue(nestedmodule.larger_than_two(number))

    @data(2, 1, 0, -1)
    def test_not_larger_than_two(self, number):
        self.assertFalse(nestedmodule.larger_than_two(number))

if __name__ == '__main__':
    unittest.main()


# This comes from
# https://technomilk.wordpress.com/2012/02/12/multiplying-python-unit-test-cases-with-different-sets-of-data/
