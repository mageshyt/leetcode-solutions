"""
<A spreadsheet is a grid with 26 columns (labeled from 'A' to 'Z') and a given number of rows. Each cell in the spreadsheet can hold an integer value between 0 and 105.

Implement the Spreadsheet class:

Spreadsheet(int rows) Initializes a spreadsheet with 26 columns (labeled 'A' to 'Z') and the specified number of rows. All cells are initially set to 0.
void setCell(String cell, int value) Sets the value of the specified cell. The cell reference is provided in the format "AX" (e.g., "A1", "B10"), where the letter represents the column (from 'A' to 'Z') and the number represents a 1-indexed row.
void resetCell(String cell) Resets the specified cell to 0.
int getValue(String formula) Evaluates a formula of the form "=X+Y", where X and Y are either cell references or non-negative integers, and returns the computed sum.
Note: If getValue references a cell that has not been explicitly set using setCell, its value is considered 0.
"""

class Spreadsheet:

    def __init__(self, rows: int):
        self.rows = rows
        self.cols = 26
        self.sheet = [[0] * self.cols for _ in range(rows)]
        

    def setCell(self, cell: str, value: int) -> None:
        col = ord(cell[0]) - ord('A') # get column index
        row = int(cell[1:]) - 1 # get row index (1-index)
        self.sheet[row][col] = value

    def resetCell(self, cell: str) -> None:
        col = ord(cell[0]) - ord('A')
        row = int(cell[1:]) - 1
        self.sheet[row][col] = 0
        

    def getValue(self, formula: str) -> int:
        formula = formula[1:]
        x, y = formula.split('+')
        def get_val(s):
            if s[0].isalpha():
                col = ord(s[0]) - ord('A')
                row = int(s[1:]) - 1
                return self.sheet[row][col]
            else:
                return int(s)
        return get_val(x) + get_val(y)

# Your Spreadsheet object will be instantiated and called as such:
# obj = Spreadsheet(rows)
# obj.setCell(cell,value)
# obj.resetCell(cell)
# param_3 = obj.getValue(formula)
