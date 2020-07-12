"""
https://leetcode.com/problems/longest-common-prefix/
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

Note:

All given inputs are in lowercase letters a-z.

"""
from typing import List

class Solution:

    def longestCommonPrefix(self, strs: List[str]) -> str:

        if not strs:
            return ""

        def getCommonPrefix(str1, str2):
            if not str1 or not str2:
                return ""
            if str1[0] == str2[0]:
                return str1[0] + getCommonPrefix(str1[1:], str2[1:])
            else:
                return ""

        common_prefix = strs[0]
        for _str in strs[1:]:
            common_prefix = getCommonPrefix(common_prefix, _str)

        return common_prefix


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["dog","racecar","car"]))