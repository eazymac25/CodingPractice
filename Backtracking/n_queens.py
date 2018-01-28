"""
The n-queens puzzle is the problem of placing n queens on an nxn chessboard such that no two queens attack each other.


Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

For example,
There exist two distinct solutions to the 4-queens puzzle:

[
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

"""


class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.n = n
        self.board = [["." for x in range(n)] for x in range(n)]
        self.results = []
        self.backtrack(0)
        return self.results
    
    def backtrack(self, col):
        if col == self.n:
            result = []
            for row in self.board:
                s = ''
                for piece in row:
                    s += piece
                result.append(s)
            self.results.append(result)
            return
        for row in xrange(self.n):
            # print self.is_valid_loc(row, col), row
            if self.is_valid_loc(row, col):
                self.board[row][col] = 'Q'
                self.backtrack(col+1)
                self.board[row][col] = '.'
    
    def is_valid_loc(self, row, col):
        for i in xrange(self.n):
            if self.board[i][col] == 'Q' or self.board[row][i] == 'Q':
                return False
        for i in xrange(self.n):
            for j in xrange(self.n):
                if i+j == row+col or i-j == row-col:
                    if self.board[i][j] == 'Q':
                        return False
        return True
