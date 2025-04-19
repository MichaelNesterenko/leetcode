from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(prev: Optional[ListNode], next: Optional[ListNode]) -> Optional[ListNode]:
            if next is None:
                return prev
            next_next = next.next
            next.next = prev
            return reverse(next, next_next)

        # next = head
        # prev = None
        # while next is not None:
        #     next_next = next.next
        #     next.next = prev
        #     prev = next
        #     next = next_next
        # return prev

        return reverse(None, head)

print(Solution().reverseList(ListNode(val = 1, next=ListNode(val = 2, next=ListNode(val = 3, next=ListNode(val = 4))))))