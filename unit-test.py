import unittest
from test_jenkins import test_jenkins


class MyFunTest(unittest.TestCase):

    def test_positive(self):
        self.assertEquals(test_jenkins(self), "Jenkins working!")

if __name__ == '__main__':
    unittest.main()
