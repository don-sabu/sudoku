import sudoku as sk
true_grid = [[3, 8, 7, 2, 4, 1, 5, 6, 9],
             [5, 2, 9, 6, 3, 7, 8, 1, 4],
             [4, 6, 1, 5, 9, 8, 2, 7, 3],
             [7, 5, 6, 8, 2, 9, 4, 3, 1],
             [9, 4, 2, 1, 5, 3, 6, 8, 7],
             [8, 1, 3, 7, 6, 4, 9, 5, 2],
             [1, 7, 4, 9, 8, 5, 3, 2, 6],
             [2, 3, 8, 4, 7, 6, 1, 9, 5],
             [6, 9, 5, 3, 1, 2, 7, 4, 8]]
print(sk.validate(true_grid))
false_grid = [[3, 8, 7, 2, 4, 1, 5, 6, 9],
              [5, 2, 9, 6, 3, 7, 8, 1, 4],
              [4, 6, 1, 5, 3, 8, 2, 7, 3],
              [7, 5, 6, 8, 3, 9, 4, 3, 1],
              [9, 4, 2, 1, 5, 3, 6, 8, 7],
              [8, 1, 3, 7, 6, 4, 9, 5, 2],
              [1, 7, 4, 9, 8, 5, 3, 2, 6],
              [2, 3, 8, 4, 7, 6, 1, 9, 5],
              [6, 9, 5, 3, 1, 2, 7, 4, 8]]
print(sk.validate(false_grid))