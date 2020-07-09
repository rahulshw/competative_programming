"""
https://leetcode.com/problems/product-of-array-except-self/
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]

Constraint: It's guaranteed that the product of the elements of any prefix or suffix of the array (including the whole array) fits in a 32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

"""
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_products = [1]*n
        backward_products = [1]*n

        for i in range(1, n):
            forward_products[i] = forward_products[i-1]*nums[i-1]

        for j in range(n-2,-1,-1):
            backward_products[j] = backward_products[j+1]*nums[j+1]

        ans = [1]*n
        for i in range(0,n):
            ans[i] = forward_products[i]*backward_products[i]

        return ans

if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))