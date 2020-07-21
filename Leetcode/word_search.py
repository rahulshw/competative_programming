"""
https://leetcode.com/explore/challenge/card/july-leetcoding-challenge/546/week-3-july-15th-july-21st/3397/
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.



Constraints:

    board and word consists only of lowercase and uppercase English letters.
    1 <= board.length <= 200
    1 <= board[i].length <= 200
    1 <= word.length <= 10^3

"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        n = len(board)
        m = len(board[0])
        visited_cell = [ [False]*m for i in range(n) ]

        for i in range(n):
            for j in range(m):
                matched = self.match_rest(board, visited_cell, (i,j), word, (n,m))
                if matched:
                    return True
        return False

    def match_rest(self, board, visited_cell, board_idx, word, sizes):
        i = board_idx[0]
        j = board_idx[1]
        n = sizes[0]
        m = sizes[1]

        if word[0] == board[i][j]:
            if word[1:]:
                visited_cell[i][j] = True
                # left
                if j > 0 and not visited_cell[i][j - 1]:
                    matched = self.match_rest(board, visited_cell, (i, j-1), word[1:], sizes)
                    if matched:
                        return True

                # right
                if j < m-1 and not visited_cell[i][j+1]:
                    matched = self.match_rest(board, visited_cell, (i, j+1), word[1:], sizes)
                    if matched:
                        return True

                # up
                if i > 0 and not visited_cell[i-1][j]:
                    matched = self.match_rest(board, visited_cell, (i-1, j), word[1:], sizes)
                    if matched:
                        return True

                # down
                if i < n-1 and not visited_cell[i+1][j]:
                    matched = self.match_rest(board, visited_cell, (i+1, j), word[1:], sizes)
                    if matched:
                        return True
                visited_cell[i][j] = False
                return False
            else:
                return True


if __name__ == "__main__":
    s = Solution()
    board = [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ]
    print(s.exist(board, "ABCCED"))
    print(s.exist(board, "SEE"))
    print(s.exist(board, "ABCB"))
    print(s.exist([["a"]],"a"))