# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def swapNodes(self, head, k):
        # Find the kth node from the beginning
        first = head
        for _ in range(k - 1):
            first = first.next

        # Find the kth node from the end using two pointers
        second = head
        runner = first
        while runner.next:
            runner = runner.next
            second = second.next

        # Swap the values
        first.val, second.val = second.val, first.val

        return head