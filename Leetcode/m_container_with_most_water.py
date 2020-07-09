# Problem: https://leetcode.com/problems/container-with-most-water/

"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

Example:

Input: [1,8,6,2,5,4,8,3,7]
Output: 49

"""
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        i = 0
        j = len(height) - 1
        while i < j:

            if height[i] < height[j]:
                max_area = max(max_area, (j - i) * height[i])
                i += 1
            else:
                max_area = max(max_area, (j - i) * height[j])
                j -= 1
        return max_area


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))