from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        left: Optional[ListNode] = head
        right: Optional[ListNode] = head
        for _ in range(n):
            right = right.next
        if right == None:
            return head.next
        while right.next:
            left, right = left.next, right.next
        left.next = left.next.next
        return head


sol = Solution()
# head = ListNode(1, ListNode(2, ListNode(
#     3, ListNode(4, ListNode(5)))))
head = ListNode(1)
print(sol.removeNthFromEnd(head, 1))
