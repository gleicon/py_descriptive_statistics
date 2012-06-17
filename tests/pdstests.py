import unittest, sys
sys.path.append("..")

from py_descriptive_statistics import Enum

class TestPyDescriptiveStatistics(unittest.TestCase):
    def setUp(self):
        self.enum = Enum([2,6,9,3,5,1,8,3,6,9,2])
    
    def test_number(self):
        self.assertEqual(self.enum.number(), 11)
    
    def test_sum(self):
        self.assertEqual(self.enum.sum(), 54)

    def test_mean(self):
        self.assertEqual(self.enum.mean(), 4.909090909090909)

    def test_median(self):
        self.assertEqual(self.enum.median(), 5.0)

    def test_variance(self):
        self.assertEqual(self.enum.variance(), 7.7190082644628095)

    def test_standard_deviation(self):
        self.assertEqual(self.enum.standard_deviation(), 2.778310325442932)

    def test_percentile(self):
        self.assertEqual(self.enum.percentile(70), 6.0)

if __name__ == '__main__':
    unittest.main()

