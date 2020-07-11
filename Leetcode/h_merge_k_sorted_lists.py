"""
https://leetcode.com/problems/merge-k-sorted-lists/
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6


"""
from typing import List
import heapq


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return 'Node(%s, next=%s)'%(self.val, self.next)


class Solution:

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        sorted_head_values = [] # sorted list of head values
        new_ll = ListNode(val=0)
        new_ll_pointer = new_ll
        count_of_empty_lists = 0

        for idx, ll in enumerate(lists):
            if ll:
                heapq.heappush(sorted_head_values, (ll.val, idx, ll))
                lists[idx] = ll.next
            else:
                count_of_empty_lists += 1

        while count_of_empty_lists < k:
            print(sorted_head_values)
            min_val_tuple = heapq.heappop(sorted_head_values)
            print(sorted_head_values)
            new_ll_pointer.next = min_val_tuple[2]
            new_ll_pointer = new_ll_pointer.next
            ll = lists[min_val_tuple[1]]
            if ll:
                heapq.heappush(sorted_head_values, (ll.val, min_val_tuple[1], ll))
                lists[min_val_tuple[1]] = ll.next
            else:
                count_of_empty_lists += 1
            print(count_of_empty_lists)

        return new_ll.next


def create_lls(lists):
    n = len(lists)
    res = []

    for _list in lists:
        node_head = ListNode(val=0)
        pointer = node_head
        for i in _list:
            pointer.next = ListNode(val=i)
            pointer = pointer.next
        res.append(node_head.next)

    return res


if __name__ == '__main__':
    input_lists = create_lls([[1,4,5],[1,3,4],[2,6]])
    input_lists = create_lls([[1]])
    print(input_lists[0])
    print(Solution().mergeKLists(input_lists))



