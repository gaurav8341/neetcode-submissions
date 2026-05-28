# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fastp, slowp = head.next, head

        while fastp and fastp.next:
            fastp = fastp.next.next
            slowp = slowp.next

            if fastp == slowp:
                return True
        
        return False