"""
Problem: https://leetcode.com/problems/trapping-rain-water/
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""


class Solution:
    def trap(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        total_water = 0
        last_min_height = 0
        last_overall_max_of_min_heights = 0
        while i < j:
            current_min_height = min(height[i], height[j])
            if current_min_height > last_overall_max_of_min_heights:
                total_water += (current_min_height - last_overall_max_of_min_heights) * (j - i)
                last_overall_max_of_min_heights = current_min_height
            print('current_min_height:%s total_water:%s i:%s j:%s last_overall_max_of_min_heights: %s' % (
            current_min_height, total_water, i, j, last_overall_max_of_min_heights))
            if height[i] < height[j]:
                total_water -= height[i]
                i += 1

            else:
                total_water -= height[j]
                j -= 1
        return total_water


if __name__ == '__main__':
    s = Solution()
    print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))