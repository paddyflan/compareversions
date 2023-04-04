import unittest
from sojern import compare_versions

class TestCompareVersions(unittest.TestCase):
    def test1(self):
        self.assertEqual(compare_versions('33','4'), 1)

    def test2(self):
        self.assertEqual(compare_versions('2','5'), -1)

    def test3(self):
        self.assertEqual(compare_versions('4.55.6','4.22.7'), 1)

    def test4(self):
        self.assertEqual(compare_versions('4.55.6.77','4.55.6.77.8'), -1)
    
    def test5(self):
        self.assertEqual(compare_versions('4.55.6.77.8','4.55.6.77'), 1)

if __name__ == '__main__':
    unittest.main()