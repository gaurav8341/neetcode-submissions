# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def reverseList(self, head: Optional[ListNode]) -> None:
        curr, prev = head, None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def reorderList(self, head: Optional[ListNode]) -> None:

        fastp, slowp = head.next, head

        while fastp and fastp.next:
            fastp = fastp.next.next
            slowp = slowp.next
        
        midpoint = slowp.next
        secondh = self.reverseList(slowp.next)
        slowp.next = None

        first = head

        while secondh:
            temp1 = first.next
            temp2 = secondh.next
            first.next = secondh
            secondh.next = temp1
            secondh = temp2
            first = temp1
        
        return 

        