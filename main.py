# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: ListNode = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = 0
        dummy = tail = ListNode(0)
        while l1 or l2 or sum:
            sum += (l1.val if l1 else 0) + (l2.val if l2 else 0)
            tail.next = ListNode(val=(sum % 10))
            tail = tail.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            sum //= 10
        return dummy.next


sol = Solution()
l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(
    4, ListNode(0, ListNode(0, ListNode(9))))))
sol.addTwoNumbers(l1, l2)
