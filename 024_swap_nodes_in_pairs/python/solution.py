from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next:
            prev_head, head, next_head = head, head.next, head.next.next
            head.next = prev_head

            prev_head.next = self.swapPairs(next_head)
        return head

Solution().swapPairs(ListNode(val = 1, next=ListNode(val = 2, next=ListNode(val = 3, next=ListNode(val = 4)))))