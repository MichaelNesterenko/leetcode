from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode(val=0)
        cur = ret
        while l1 or l2:
            sum = cur.val + (l1.val if l1 else 0) + (l2.val if l2 else 0)
            cur.val = sum % 10

            fwd = sum > 9
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            cur.next = ListNode(val = 1 if fwd else 0) if fwd or l1 or l2 else None
            cur = cur.next
        return ret

def as_linked(l: List[int]) -> ListNode:
    return ListNode(val = l[0], next = as_linked(l[1:len(l)])) if l else None

print (Solution().addTwoNumbers(as_linked([9,9,9,9,9,9,9]), as_linked([9,9,9,9])))
