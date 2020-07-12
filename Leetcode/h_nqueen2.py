"""
https://leetcode.com/problems/n-queens-ii/
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return the number of distinct solutions to the n-queens puzzle.

Example:

Input: 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown below.
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
from typing import List, Tuple


class Solution:
    def totalNQueens(self, n: int) -> int:
        solutions = self._solveNQueens(n, 0)
        return len(solutions)

    def _solveNQueens(self, n, hor_level) -> List[List[Tuple]]:
        new_solutions = []
        if hor_level == n-1:
            for i in range(n):
                new_solutions.append([(hor_level, i)])
        else:
            last_solutions = self._solveNQueens(n, hor_level+1)

            for solution in last_solutions:
                for i in range(n):
                    if self.queenPlacable((hor_level, i), solution):
                        new_solutions.append(solution + [(hor_level, i)])

        #print(new_solutions)
        return new_solutions

    def queenPlacable(self, index_tuple, pre_index_tuples):
        for pre_index_tuple in pre_index_tuples:
            if index_tuple[0] == pre_index_tuple[0]:
                return False
            elif index_tuple[1] == pre_index_tuple[1]:
                return False
            elif abs(index_tuple[1] - pre_index_tuple[1]) == abs(index_tuple[0] - pre_index_tuple[0]):
                return False
        #print(index_tuple, pre_index_tuples)
        return True


if __name__ == '__main__':
    print(Solution().totalNQueens(n=5))
