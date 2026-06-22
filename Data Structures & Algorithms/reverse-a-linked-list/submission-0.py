# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = None, head

        while curr:
            nxt = curr.next #store the original next node
            curr.next = prev # current node points backward
            prev = curr # head of reversed portion is now this node
            curr = nxt # moves curr to the next unreversed node
        return prev