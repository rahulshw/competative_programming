#Problem: https://leetcode.com/problems/integer-replacement/

"""
 Given a positive integer n and you can do operations as follow:

    If n is even, replace n with n/2.
    If n is odd, you can replace n with either n + 1 or n - 1.

What is the minimum number of replacements needed for n to become 1?

Example 1:

Input:
8

Output:
3

Explanation:
8 -> 4 -> 2 -> 1

Example 2:

Input:
7

Output:
4

Explanation:
7 -> 8 -> 4 -> 2 -> 1
or
7 -> 6 -> 3 -> 2 -> 1

"""


class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        elif n == 3:
            return 2
        elif self.if_even(n):
            return 1 + self.integerReplacement(n // 2)
        else:
            num1 = (n+1)//2
            num2 = (n-1)//2
            if self.if_even(num1):
                return 2 + self.integerReplacement(num1)
            else:
                return 2 + self.integerReplacement(num2)

    def if_even(self, n):
        return n == n >> 1 << 1


if __name__ == '__main__':
    s = Solution()

    print(s.integerReplacement(7))



