import unittest

from seq_optimizer import longest_common

class TestLongestCommon(unittest.TestCase):

    def test_longest_common(self):
        # Test case 1: List of lists with common subsequence
        seq1 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = longest_common(seq1)
        expected = [1,2,3,4,5]
        self.assertEqual(result, expected)
        
        # Test case 2: List of lists with no common subsequence
        seq2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = longest_common(seq2)
        expected = []
        self.assertEqual(result, expected)
        
        # Test case 3: List of lists with identical sequences
        seq3 = [[1, 2, 3], [1, 2, 3], [1, 2, 3]]
        result = longest_common(seq3)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)
        
        # Test case 4: List with empty subsequences
        seq4 = [[], [], []]
        result = longest_common(seq4)
        expected = []
        self.assertEqual(result, expected)
        
        # Test case 5: Single sequence in the list
        seq5 = [[1, 2, 3]]
        result = longest_common(seq5)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
