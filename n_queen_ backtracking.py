class queen():
    def __init__(self, board_size):
        self.board = board
        self.board_size = board_size

    #backtracking algorithn to place queen one by one safely on the board
    def place_queens(self):
        

    #print n*n board
    def print_board(self, board = None):
        for row in self.board:
            for col in self.board:
                if(row == board[col]):
                    print("Q", end = "\t")
                else:
                    print('_', end="\t")
            print("\n")


board= [0,1,2,3,4]
board1= queen(board)
board1.print_board(board)