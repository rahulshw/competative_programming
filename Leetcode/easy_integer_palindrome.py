# promblem: https://leetcode.com/problems/palindrome-number/
import math
class Solution:
    def isPalindrome(self, x: int, digit_count: int = None, divisor: int = None) -> bool:
        if x < 0:
            return False
        if x < 10:
            return True

        if not digit_count:
            digit_count = self.calculateDigits(x)

        divisor_for_first_part = 10 ** (math.ceil(digit_count/2))
        divisor_for_second_part = 10 ** (math.floor(digit_count/2))

        first_part = self.reverse_digits(x // divisor_for_first_part)
        last_part = x % divisor_for_second_part

        print(first_part, last_part)

        if first_part == last_part:
            return True
        else:
            return False

    def calculateDigits(self, x: int):
        digit_count = 1
        while x // 10 != 0:
            digit_count += 1
            x = x // 10
        print(digit_count)
        return digit_count

    def reverse_digits(self, x: int):
        res = x % 10
        while x // 10 != 0:
            x = x // 10
            last_digit = x % 10
            res = res*10 + last_digit
        return res


if __name__ == '__main__':
    inputs = [121, 123321, 1001, 1223356, 0, 1000021, 1210345]
    s = Solution()
    for input in inputs:
        print(s.isPalindrome(input))