"""
https://leetcode.com/problems/reverse-words-in-a-string/
Given an input string, reverse the string word by word.



Example 1:

Input: "the sky is blue"
Output: "blue is sky the"

Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.

Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.



Note:

    A word is defined as a sequence of non-space characters.
    Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
    You need to reduce multiple spaces between two words to a single space in the reversed string.



Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
"""


class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""

        for idx,i in enumerate(s):
            if s[idx] == " ":
                break

        predecessors = self.reverseWords(s[idx+1:])

        if not predecessors:
            return s.strip()
        else:
            return (predecessors + " " + s[0:idx]).strip()

if __name__ == '__main__':
    print(Solution().reverseWords("  hello world!  "))