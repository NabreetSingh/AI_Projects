from __future__ import print_function
class queen():
    def __init__(self, board_size):
        self.board = board
        self.board_size = board_size

    #backtracking algorithn to place queen one by one safely on the board
    def place_queens(self):
        pass

    def count_conflicts(self, column):
        count = 0

        #the same row
        for col in self.board:
            if(col == column):
                pass
            elif(board[column] == board[col]):
                count = count + 1

        #the postivie diagonal
        for col in self.board:
            if (col < column):
                if (board[col] == board[column] - (column - col)):
                    count = count +1
            elif (col > column):
                if (board[col] == board[column] + (column - col)):
                    count = count +1 

        #the negative diagonal
        for col in self.board:
            if (col < column):
                if (board[col] == board[column] + (column - col)):
                    count = count + 1
            elif (col > column):
                if (board[col] == board[column] - (column - col)):
                    count = count +1
        
        return count

    #print n*n board
    def print_board(self, board = None):
        for row in self.board:
            for col in self.board:
                if(row == board[col]):
                    print("Q", end = '\t')
                else:
                    print('.', end ='\t')
            print("\n")


board= [0,1,2,3,4]
board1= queen(board)
board1.print_board(board)