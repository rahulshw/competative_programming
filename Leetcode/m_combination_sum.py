"""
https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]



Constraints:

    1 <= candidates.length <= 30
    1 <= candidates[i] <= 200
    Each element of candidate is unique.
    1 <= target <= 500


"""
from typing import List

class Solution:

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        print(target, candidates)
        if target == 0 :
            return [[]]
        if target < 0:
            return None
        if target > 0 and not candidates:
            return None
        res_list = []
        for idx, candidate in enumerate(candidates):
            res = target - candidate
            candidate_list = [candidate]
            while res >= 0:
                solutions = self.combinationSum(candidates[idx+1:], res)
                print(candidate_list, solutions)
                if solutions is not None:
                        res_list += [candidate_list + solution for solution in solutions]

                res = res - candidate
                candidate_list.append(candidate)
        print('returning: %s'%res_list)
        return res_list


if __name__ == '__main__':
    print(Solution().combinationSum(candidates=[2,3,5], target=8))