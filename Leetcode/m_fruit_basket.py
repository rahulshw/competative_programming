"""
https://leetcode.com/problems/fruit-into-baskets/
In a row of trees, the i-th tree produces fruit with type tree[i].

You start at any tree of your choice, then repeatedly perform the following steps:

    Add one piece of fruit from this tree to your baskets.  If you cannot, stop.
    Move to the next tree to the right of the current tree.  If there is no tree to the right, stop.

Note that you do not have any choice after the initial choice of starting tree: you must perform step 1, then step 2, then back to step 1, then step 2, and so on until you stop.

You have two baskets, and each basket can carry any quantity of fruit, but you want each basket to only carry one type of fruit each.

What is the total amount of fruit you can collect with this procedure?



Example 1:

Input: [1,2,1]
Output: 3
Explanation: We can collect [1,2,1].

Example 2:

Input: [0,1,2,2]
Output: 3
Explanation: We can collect [1,2,2].
If we started at the first tree, we would only collect [0, 1].

Example 3:

Input: [1,2,3,2,2]
Output: 4
Explanation: We can collect [2,3,2,2].
If we started at the first tree, we would only collect [1, 2].

Example 4:

Input: [3,3,3,1,2,1,1,2,3,3,4]
Output: 5
Explanation: We can collect [1,2,1,1,2].
If we started at the first tree or the eighth tree, we would only collect 4 fruits.



Note:

    1 <= tree.length <= 40000
    0 <= tree[i] < tree.length


"""
from typing import List


class Solution:

    def totalFruit(self, tree: List[int]) -> int:
        n = len(tree)

        if n == 1:
            return 1
        elif n == 2:
            return 2

        basket_fruits = []

        basket_fruits_count = [0, 0]

        count_after_last_basket_fruit = [0, 0]

        i = 0

        max_count = -1
        while i < n:
            if len(basket_fruits) < 2:
                if tree[i] in basket_fruits: # means there is only one kind of fruit encountered
                    idx = basket_fruits.index(tree[i])
                    basket_fruits_count[idx] += 1
                else:
                    basket_fruits.append(tree[i])
                    if len(basket_fruits) == 2:
                        count_after_last_basket_fruit[0] += 1
                        idx = 1
                    else:
                        idx = 0
                    basket_fruits_count[idx] += 1
            else:
                if tree[i] in basket_fruits:
                    idx = basket_fruits.index(tree[i])
                    basket_fruits_count[idx] += 1
                    count_after_last_basket_fruit[idx] = 0
                    count_after_last_basket_fruit[(idx+1)%2] += 1
                else:
                    oldest_fruit_idx = (last_fruit_idx+1)%2
                    idx = oldest_fruit_idx
                    basket_fruits[idx] = tree[i]
                    basket_fruits_count[idx] = 1
                    basket_fruits_count[last_fruit_idx] = count_after_last_basket_fruit[idx]
                    count_after_last_basket_fruit[last_fruit_idx] = 1
                    count_after_last_basket_fruit[idx] = 0

            if sum(basket_fruits_count) > max_count:
                max_count = sum(basket_fruits_count)

            last_fruit_idx = idx
            i += 1

        return max_count


if __name__ == '__main__':
    print(Solution().totalFruit([3,3,3,1,2,1,1,2,3,3,4]))
    print(Solution().totalFruit([1,0,0,0,1,0,4,0,4]))