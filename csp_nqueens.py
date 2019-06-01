# Uncomment following line if you are not running python3
#from __future__ import print_function
import random
import time
start = time.time()

class queen():
    def __init__(self, board_size):
        self.board_size = int(board_size)
        self.board = [[]] * self.board_size
        
    def main(self):
        if(self.place_queens(0) == True):
            self.print_board()
    

    #backtracking algorithn to place queen one by one safely on the board
    def place_queens(self, column):
        if([] in self.board):
            pass
        else:
            return True

        row = 0
        #backtracking with recursion
        while(row < self.board_size):
            self.board[column] = row
            if(self.is_safe(column) == True and self.place_queens(self.most_constrained_column(self.board)) == True):
                return True
            self.board[column] = []
            row = row + 1
        return False

    #find most constrained columns
    def most_constrained_column(self, board):
        most_constrained_columns = []
        least_constraints = 0

        for col in range(self.board_size):
            if(board[col] != []):
                continue
            if(self.no_of_constrained_rows(col) > least_constraints):
                least_constraints = self.no_of_constrained_rows(col)
                most_constrained_columns = []
                most_constrained_columns.append(col)
            elif(self.no_of_constrained_rows(col) == least_constraints):
                most_constrained_columns.append(col)
        if(len(most_constrained_columns) == 0):
            return
        else:
            return most_constrained_columns[0]

    #count number of constrained row in a specific column
    def no_of_constrained_rows(self,column):
        initial_state = self.board[column]
        count = 0

        for r in range(0,self.board_size):
            self.board[column] = r
            if(self.is_safe(column) == False):
                count = count + 1
        self.board[column] = initial_state
        return count
            


    
    #return true if queen is safe else false in a specific column
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
                if(row == self.board[col]):
                    print("Q", end = '\t')
                else:
                    print('.', end ='\t')
            print("\n")

board_size = input("Enter the size of the board: ")   
build1 = queen(board_size);
build1.main()

end = time.time()
print("Solution found in :", end-start)