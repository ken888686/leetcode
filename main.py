from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val: int = val
        self.next: Optional[ListNode] = next


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow


sol = Solution()
head = ListNode(1, ListNode(2, ListNode(
    3, ListNode(4, ListNode(5)))))
print(sol.middleNode(head))
