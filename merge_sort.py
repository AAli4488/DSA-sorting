"""
LeetCode 23. Merge k Sorted Lists  (Hard)
https://leetcode.com/problems/merge-k-sorted-lists/

Question:
You are given an array of k linked-lists `lists`, each linked-list is sorted
in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
    Input:  lists = [[1,4,5],[1,3,4],[2,6]]
    Output: [1,1,2,3,4,4,5,6]
    Explanation: The linked-lists are:
        1->4->5,
        1->3->4,
        2->6
    Merging them into one sorted list: 1->1->2->3->4->4->5->6

Example 2:
    Input:  lists = []
    Output: []

Example 3:
    Input:  lists = [[]]
    Output: []

Constraints:
    k == lists.length
    0 <= k <= 10^4
    0 <= lists[i].length <= 500
    -10^4 <= lists[i][j] <= 10^4
    lists[i] is sorted in ascending order.
    The sum of lists[i].length will not exceed 10^4.

Approach: Min-Heap
    Push the head of every list into a min-heap. Repeatedly pop the smallest
    node, attach it to the result, and push that node's next node.

Complexity:
    Time:  O(N log k)   (N = total nodes, k = number of lists)
    Space: O(k)
"""

import heapq
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        # Push the head of each non-empty list: (value, list index, node)
        # The index breaks ties so Python never compares ListNode objects.
        for i, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, i, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, i, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))

        return dummy.next


# ---------- Helpers for running locally ----------

def build_list(values):
    """Convert a Python list into a linked list and return its head."""
    dummy = ListNode(0)
    curr = dummy
    for v in values:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def to_list(head):
    """Convert a linked list back into a Python list."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------- Test cases ----------

if __name__ == "__main__":
    sol = Solution()

    tests = [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[], [1], []], [1]),
        ([[-2, -1, -1, -1], [], [5]], [-2, -1, -1, -1, 5]),
    ]

    for inp, expected in tests:
        lists = [build_list(arr) for arr in inp]
        result = to_list(sol.mergeKLists(lists))
        status = "PASS" if result == expected else "FAIL"
        print(f"{status} | input={inp} | output={result} | expected={expected}")
