# Problem: https://leetcode.com/problems/multiply-strings/

"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

Note:

    The length of both num1 and num2 is < 110.
    Both num1 and num2 contain only digits 0-9.
    Both num1 and num2 do not contain any leading zero, except the number 0 itself.
    You must not use any built-in BigInteger library or convert the inputs to integer directly.


"""

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        l1 = len(num1)
        l2 = len(num2)
        result = [0]
        result_length = 1
        for idx, i in enumerate(range(-1, -l1-1, -1)):
            res_digits = []
            res_digits_length = 0
            carry = 0

            for j in range(-1, -l2-1, -1):
                res = (int(num1[i])*int(num2[j])) + carry
                carry = res//10
                res_digits.append(res%10)
                res_digits_length += 1

            if carry > 0:
                res_digits.append(carry)
                res_digits_length += 1

            if res_digits[-1] > 0:
                res_digits = [0] * idx + res_digits
                res_digits_length += idx

            print(res_digits)

            result, result_length = self.add(result, res_digits, result_length, res_digits_length)

        result.reverse()

        def remove_leading_zeros(list1):
            for idx,i in enumerate(list1):
                if i != 0:
                    break
            return list1[idx:]

        return ''.join(''.join([str(x) for x in remove_leading_zeros(result)]))

    def add(self, _list1, _list2, _l1, _l2):
        print(_list1, _list2)
        new_list = []
        new_list_length = 0
        carry = 0

        if _l2 < _l1:
            l2 = _l1
            l1 = _l2
            list1 = _list2
            list2 = _list1
        else:
            l2 = _l2
            l1 = _l1
            list1 = _list1
            list2 = _list2

        for idx, i in enumerate(list1):
            j = list2[idx]
            s = i + j + carry
            carry = s // 10
            new_list.append(s % 10)
            new_list_length += 1

        idx += 1
        while idx < l2:
            s = carry + list2[idx]
            carry = s //10
            new_list.append(s % 10)
            new_list_length += 1
            idx += 1

        if carry:
            new_list.append(carry)
            new_list_length += 1


        print(new_list)
        return new_list, new_list_length


if __name__ == '__main__':
    s = Solution()
    print(s.multiply('0', '1234'))


