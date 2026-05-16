# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def get_kth(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr


    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # break list such that each has k elem.
        # Reverse each and add to result list

        dummy = ListNode(0, head)
        groupPrev = dummy # prev of the group
        
        while True:
            # get kth elem in group
            kth = self.get_kth(groupPrev, k)
            if not kth:
                break
            
            groupNext = kth.next
            
            # we have group prev and we have kth elem and next greoup elem
            prev, curr = groupNext, groupPrev.next
            while curr != groupNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
            
            tmp = groupPrev.next
            groupPrev.next = kth
            groupPrev = tmp
        return dummy.next

        