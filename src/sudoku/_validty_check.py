class _ValidGrid:
    def __int__(self, grid):
        self.grid = grid

    def _isValidList(self, unique_list):
        if len(unique_list) != len(set(unique_list)):
            return False
        count = 0
        for i in unique_list:
            if 0 < i < 10:
                count += 1
        if count != 9:
            return False
        return True

    def _boxValid(self):
        for i in range(3):
            for j in range(3):
                box = []
                for x in range(i * 3, i * 3 + 3):
                    for y in range(j * 3, j * 3 + 3):
                        box.append(self.grid[x][y])
                if not self._isValidList(box):
                    return False
        return True

    def _columnValid(self):
        for j in range(9):
            column = []
            for i in range(9):
                column.append(self.grid[i][j])
            if not self._isValidList(column):
                return False
        return True

    def _rowValid(self):
        for row in self.grid:
            if not self._isValidList(row):
                return False
        return True


def isValid(table):
    return rowValid(table) and columnValid(table) and boxValid(table)
