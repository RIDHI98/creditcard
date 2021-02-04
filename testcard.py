from creditcard12345 import check_cvv
import unittest

class card(unittest.TestCase):

    def test_cvv(self):
        self.assertEqual(self.check_cvv(789),True)

    
if __name__ == "__main__":
    unittest.main()
    
