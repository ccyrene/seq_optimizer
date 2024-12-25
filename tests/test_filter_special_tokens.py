import unittest

from seq_optimizer import filter_special_tokens

class TestFilterSpecialToken(unittest.TestCase):
    
    def setUp(self):
        self.special_tokens = list(range(50257, 50365))

    def test_filter_special_tokens(self):
        # Test case 1: Head speacial tokens
        seq1 = [50258, 50289, 50360, 50364, 4131, 23398, 17297, 12774, 5104]
        result = filter_special_tokens(seq1, self.special_tokens)
        expected = [4131, 23398, 17297, 12774, 5104]
        self.assertEqual(result, expected)
        
        # Test case 2: Head & Tail special tokens
        seq2 = [50258, 50289, 50360, 50364, 8055, 8163, 4294, 8055, 50257, 50257, 50257, 50257, 50257]
        result = filter_special_tokens(seq2, self.special_tokens)
        expected = [8055, 8163, 4294, 8055]
        self.assertEqual(result, expected)
        
        # Test case 3: Tail special tokens
        seq3 = [100, 38206, 17071, 47376, 5914, 100, 839, 101, 4131, 6192, 50257, 50257]
        result = filter_special_tokens(seq3, self.special_tokens)
        expected = [100, 38206, 17071, 47376, 5914, 100, 839, 101, 4131, 6192]
        self.assertEqual(result, expected)
        
if __name__ == '__main__':
    unittest.main()