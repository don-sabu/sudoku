from . import sudokuGenerator as sg


def generate():
    sample = sg.Generator.generate_sudoku()
    return sample
