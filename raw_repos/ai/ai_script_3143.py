import unittest

class TestBubbleSort(unittest.TestCase):
    def test_sort(self):
        arr = [5, 2, 3, 7, 1]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 5, 7])

if __name__ == '__main__':
    unittest.main()