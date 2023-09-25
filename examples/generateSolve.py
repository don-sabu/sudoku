import sudoku as sk


grid = sk.generate()
print("Generated grid:")
print(grid)

solvedGrid = sk.solve(grid)
print("Solved Grid:")
print(solvedGrid)
print(sk.validate(solvedGrid))