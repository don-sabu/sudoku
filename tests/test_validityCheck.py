import unittest
from src import sudoku


class TestSudokuValidator(unittest.TestCase):
    def test_generate_sudoku_positive(self):
        sudoku_table = [[3, 8, 7, 2, 4, 1, 5, 6, 9],
                        [5, 2, 9, 6, 3, 7, 8, 1, 4],
                        [4, 6, 1, 5, 9, 8, 2, 7, 3],
                        [7, 5, 6, 8, 2, 9, 4, 3, 1],
                        [9, 4, 2, 1, 5, 3, 6, 8, 7],
                        [8, 1, 3, 7, 6, 4, 9, 5, 2],
                        [1, 7, 4, 9, 8, 5, 3, 2, 6],
                        [2, 3, 8, 4, 7, 6, 1, 9, 5],
                        [6, 9, 5, 3, 1, 2, 7, 4, 8]]
        result = sudoku.validate(sudoku_table)
        self.assertIsNotNone(result)  # Check if the result is not None
        self.assertIsInstance(result, bool)  # Check if the result is a string
        self.assertTrue(result)

    def test_generate_sudoku_negative(self):
        sudoku_table = [[6, 8, 7, 2, 4, 1, 5, 6, 9],
                        [8, 2, 9, 6, 3, 7, 8, 1, 4],
                        [4, 6, 1, 5, 9, 8, 2, 7, 3],
                        [7, 5, 6, 8, 2, 9, 4, 3, 1],
                        [9, 4, 2, 1, 5, 3, 6, 8, 7],
                        [8, 1, 3, 7, 6, 4, 9, 5, 2],
                        [1, 7, 4, 9, 8, 5, 3, 2, 6],
                        [2, 3, 8, 4, 7, 6, 1, 9, 5],
                        [6, 9, 5, 3, 1, 2, 7, 4, 8]]
        result = sudoku.validate(sudoku_table)
        self.assertIsNotNone(result)  # Check if the result is not None
        self.assertIsInstance(result, bool)  # Check if the result is a string
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
