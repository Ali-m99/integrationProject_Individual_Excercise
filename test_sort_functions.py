import unittest
from integerationProject_excercise import*

class TestSortingFunctions(unittest.TestCase):

    def test_bubble_sort_integers(self):
        self.assertEqual(bubbleSort([42, 17, 5, 88, 23]), [5, 17, 23, 42, 88])
        self.assertEqual(bubbleSort([]), [])
        self.assertEqual(bubbleSort([1]), [1])
        self.assertEqual(bubbleSort([1, 2, 3]), [1, 2, 3])
        self.assertEqual(bubbleSort([4, 5, 5, 4]), [4, 4, 5, 5])

if __name__ == "__main__":
    unittest.main()