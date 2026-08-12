# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        s = f = head

        while f and f.next:
            f = f.next.next
            s = s.next

        prev = temp = None
        while s:
            temp = s.next
            s.next = prev
            prev = s
            s = temp

        left, right = head, prev
        while right:
            if left.val != right.val: return False
            left = left.next
            right = right.next
        return True