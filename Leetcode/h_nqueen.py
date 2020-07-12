"""
https://leetcode.com/problems/n-queens/
The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.

Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:

Input: 4
Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.


"""
from typing import List, Tuple


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = self._solveNQueens(n, 0)
        if not solutions:
            return []
        results = []
        for solution in solutions:
            result = []
            for i in range(n):
                str_line = ""
                for j in range(n):
                    if (i,j) in solution:
                        str_line += 'Q'
                    else:
                        str_line += '.'
                result.append(str_line)
            results.append(result)
        return results

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
    for i in Solution().solveNQueens(n=5):
        for j in i:
            print(j)
        print('\n')
