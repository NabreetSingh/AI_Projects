# NQueens

The NQueen problem is to place N number of queen on an NxN chess board without having attack on ohter queens i.e no queen can be on the same column, row or diagonal of other queen. I'll be implementing using follwing algorithms:

Backtracking: This a brute-force type search in which queen is placed one by one in different columns, staring form left most column. If there is a safe row in a columns in which a queen can be place then the algorithm return true and goes further to place another queen until all queens are palce and if no safe row is found in a column it backtracks and return false.

Most Cosntrained Heuristic: In this search, queen is place in that column first which has least number of safe rows(least no. of valid choices).
