class QueenChessBoard:
    def __init__(self, size):
        # board has dimensions size x size
        self.size = size
        # columns[r] is a number c if a queen is placed at row r and column c.
        # columns[r] is out of range if no queen is place in row r.
        # Thus after all queens are placed, they will be at positions
        # (columns[0], 0), (columns[1], 1), ... (columns[size - 1], size - 1)
        self.columns = []
 
    def get_size(self):
        return self.size
 
    def get_queens_count(self):
        return len(self.columns)
 
    def place_in_next_row(self, column):
        self.columns.append(column)
 
    def remove_in_current_row(self):
        return self.columns.pop()
 
    def is_this_column_safe_in_next_row(self, column):
        # index of next row
        row = len(self.columns)
 
        # check column
        for queen_column in self.columns:
            if column == queen_column:
                return False
 
        # check diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if queen_column - queen_row == column - row:
                return False
 
        # check other diagonal
        for queen_row, queen_column in enumerate(self.columns):
            if ((self.size - queen_column) - queen_row
                == (self.size - column) - row):
                return False
 
        return True
 
    def display(self):
        for row in range(self.size):
            for column in range(self.size):
                if column == self.columns[row]:
                    print('Q', end=' ')
                else:
                    print('.', end=' ')
            print()
 
 
def print_all_solutions_to_n_queen(size):
    """Display a chessboard for each possible configuration of placing n queens
    on an n x n chessboard where n = size and print the number of such
    configurations."""
    board = QueenChessBoard(size)
    number_of_solutions = print_all_solutions_helper(board)
    print('Number of solutions:', number_of_solutions)
 
def print_all_solutions_helper(board):
    """Display a chessboard for each possible configuration of filling the given
    board with queens and return the number of such configurations."""
    size = board.get_size()
 
    # if board is full, display solution
    if size == board.get_queens_count():
        board.display()
        print()
        return 1
 
    number_of_solutions = 0
    # place queen in next row
    for column in range(size):
        if board.is_this_column_safe_in_next_row(column):
            board.place_in_next_row(column)
            number_of_solutions += print_all_solutions_helper(board)
            board.remove_in_current_row()
 
    return number_of_solutions
 
 
n = int(input('Enter n: '))
print_all_solutions_to_n_queen(n)
