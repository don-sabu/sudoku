from . import validtyCheck
from . import sudokuGenerator
from . import sudokuSolver


def solve(grid):
    return sudokuSolver.solver(grid)


def generate():
    return sudokuGenerator.Generator.generate_sudoku()


def validate(grid):
    return validtyCheck.isValid(grid)
