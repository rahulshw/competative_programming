"""
https://leetcode.com/problems/generate-parentheses/
 Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""

"""
First and last parenthesis will always be there. We have to find a different combinations of '(' and ')' such that all of them are used.  
"""


from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        return self.generate_combinations(n, open_braces=n, closed_braces=n)

    def generate_combinations(self, full_count, open_braces: int, closed_braces: int) -> List[str]:
        if open_braces == 0:
            return [')'*closed_braces]

        if closed_braces == 0:
            return ['('*open_braces]

        result = []

        result1 = self.generate_combinations(full_count, open_braces-1, closed_braces)

        for i in result1:
            result.append('(' + i)

        if full_count - open_braces > full_count - closed_braces:
            result2 = self.generate_combinations(full_count, open_braces, closed_braces-1)

            for i in result2:
                result.append(')' + i)


        return result


if __name__ == '__main__':
    print(Solution().generateParenthesis(n=3))
