# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s = f = head

        while f and f.next:
            f = f.next.next
            s = s.next
            if s == f: break
        else: return None

        s2 = head
        while s2 != f:
            s2 = s2.next
            f = f.next

        return s2
