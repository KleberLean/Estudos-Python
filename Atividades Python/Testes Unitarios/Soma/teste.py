import unittest
from calc import soma, subtracao

class TestCalculadora(unittest.TestCase):
    def test_soma(self):
        self.assertEqual (soma(2, 3), 5)

        
    def test_subtracao(self):
        self.assertEqual (subtracao(10, 5), 5)

if __name__ =="__main__":
    unittest.main()