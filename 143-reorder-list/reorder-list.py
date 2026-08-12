# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        d = ListNode()
        s = f = head

        while f and f.next:
            s = s.next
            f = f.next.next

        curr = s.next
        prev = s.next = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        first, curr = head, prev
        while curr:
            tmp1, tmp2 = first.next, curr.next
            first.next = curr
            curr.next = tmp1
            first = tmp1
            curr = tmp2
        