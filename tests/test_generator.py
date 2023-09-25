import unittest
from src import sudoku


class TestSudokuGenerator(unittest.TestCase):
    def test_generate_sudoku(self):
        result = sudoku.generate()
        self.assertIsNotNone(result)  # Check if the result is not None
        self.assertIsInstance(result, list)  # Check if the result is a string
        self.assertTrue(len(result) > 0)


if __name__ == '__main__':
    unittest.main()
