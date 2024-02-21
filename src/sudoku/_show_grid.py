def printer():
    print("Sudoku!!!!")
    # function to show sudoku grid


class ShowBoard:
    def __init__(self, grid, box_width, box_height):
        self.grid = grid
        self.width = box_width
        self.height = box_height

    def _createFormattedBoard(self):
        """

        :parameter:
        :return:
        """
        board = self.grid
        table = "Sudoku!!!!"
        return table

    def _createFormattedPrefix(self):
        width = self.width
        height = self.height
        size = width * height
        pass

    def showBoard(self):
        print(self._createFormattedBoard())

    def showBoardDetails(self):
        pass
