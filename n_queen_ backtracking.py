from __future__ import print_function
class queen():
    def __init__(self, board_size):
        self.board = []*board_size
        self.board_size = board_size
       
    def main(self):
        if(self.place_queens(0) == True):
            self.print_board(self.board)

    #backtracking algorithn to place queen one by one safely on the board
    def place_queens(self, column):
        if(len(self.board) == self.board_size):
                return True

        row = 0
        
        while(row < self.board_size):
            self.board.append(row)
            if(self.is_safe(column) == True and self.place_queens(column + 1) == True):
                return True
            self.board.pop()
            row = row + 1
        return False
       

    def is_safe(self, column):
        count = 0
        if(len(self.board) < column):
            return True

        #the same row
        for col in range(0,len(self.board)):
            if(col == column):
                continue
            elif(self.board[column] == self.board[col]):
                count = count + 1

        #the postivie diagonal
        for col in range(0,len(self.board)):
            if (col < column):
                if (self.board[col] == self.board[column] - (column - col)):
                    count = count +1
            elif (col > column):
                if (self.board[col] == self.board[column] + (column - col)):
                    count = count +1 

        #the negative diagonal
        for col in range(0,len(self.board)):
            if (col < column):
                if (self.board[col] == self.board[column] + (column - col)):
                    count = count + 1
            elif (col > column):
                if (self.board[col] == self.board[column] - (column - col)):
                    count = count +1
        
        if (count == 0):
            return True 
        else:
            return False

    #print n*n board
    def print_board(self, board = None):
        for row in self.board:
            for col in self.board:
                if(row == board[col]):
                    print("Q", end = '\t')
                else:
                    print('.', end ='\t')
            print("\n")
        
build1 = queen(4);
build1.main();