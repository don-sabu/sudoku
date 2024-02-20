from . import _validty_check
from . import _sudoku_generator
from . import _sudoku_solver
from . import _show_grid


def solve(grid):
    return _sudoku_solver.solver(grid)


def generate():
    return _sudoku_generator.Generator.generate_sudoku()


def validate(grid):
    return _validty_check.isValid(grid)


def show():
    return _show_grid.printer()
