# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.recursion(head)
    
    def iteration(self, head: Optional[ListNode]) -> Optional[ListNode]:

        curr = head
        # nextn = curr.next
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        return prev
    
    def recursion(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None
        
        newhead = head

        if head.next:
            newhead = self.recursion(head.next)
            head.next.next = head
        head.next = None

        return newhead

