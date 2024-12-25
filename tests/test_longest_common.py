import unittest

from seq_optimizer import longest_common

class TestLongestCommon(unittest.TestCase):

    def test_longest_common(self):
        # Test case 1: List of lists with common subsequence
        seq1 = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
        result = longest_common(seq1)
        expected = [1, 2, 3, 4, 5]
        self.assertEqual(result, expected)
        
        # Test case 2: List of lists with no common subsequence
        seq2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = longest_common(seq2)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9]
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
        
        # Test case 6: Single Element in Each Sequence
        seq6 = [[1], [2], [3]]
        result = longest_common(seq6)
        expected = [1, 2, 3]
        self.assertEqual(result, expected)
        
        # Test case 7: Sequences with Partial Overlaps
        seq7 = [[1, 2, 3], [3, 4], [4]]
        result = longest_common(seq7)
        expected = [1, 2, 3, 3, 4, 4]
        self.assertEqual(result, expected)
        
        # Test case 8: Sequences with No Overlaps
        seq8 = [[1, 2], [3, 4], [5,6]]
        result = longest_common(seq8)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)
        
        # Test case 9: Nested Sequences
        seq9 = [[1, 2, 3, 4, 5], [2, 3, 4], [1, 2], [5]]
        result = longest_common(seq9)
        expected = [1, 2, 3, 4, 1, 2, 5]
        self.assertEqual(result, expected)
        
        # Test case 10: Empty Sequences in Between
        seq10 = [[1, 2, 3], [], [4, 5, 6]]
        result = longest_common(seq10)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(result, expected)
        
        # Test case 11: Alternating Overlaps
        seq11 = [[1, 2], [2, 3], [5, 6], [6, 6]]
        result = longest_common(seq11)
        expected = [1, 2, 2, 3, 5, 6, 6, 6]
        self.assertEqual(result, expected)
        
        # Test case 12: Random Sequences with Repeated Numbers
        seq12 = [[1, 2, 3, 3, 3, 4], [3, 3, 3, 4, 5], [4, 5, 6, 7]]
        result = longest_common(seq12)
        expected = [1, 2, 3, 3, 3, 4, 5, 6, 7]
        self.assertEqual(result, expected)
        
        # Test case 13: Long Sequences
        seq13 = [list(range(1, 100)), list(range(50, 150)), list(range(120, 200))]
        result = longest_common(seq13)
        expected = list(range(1, 200))
        self.assertEqual(result, expected)
        
        # Test case 14: Natative element sequences
        seq13 = [[-2, -1, 0], [0, 1, 2], [2, 3, 4]]
        result = longest_common(seq13)
        expected = [-2, -1, 0, 0, 1, 2, 2, 3, 4]
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
