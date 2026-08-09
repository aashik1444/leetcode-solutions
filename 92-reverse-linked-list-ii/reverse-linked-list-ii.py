# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev, curr = dummy, head

        for i in range(left - 1):
            prev = curr
            curr = curr.next

        rev_prev = None

        for i in range(right - left + 1):
            tmp = curr.next
            curr.next =rev_prev
            rev_prev = curr
            curr = tmp

        prev.next.next = curr
        prev.next = rev_prev

        return dummy.next