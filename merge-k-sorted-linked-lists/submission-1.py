# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq

class NodeWrapper:
    def __init__(self, Node:ListNode):
        self.node = Node

    def __lt__(self, other):
        return self.node.val < other.node.val

class Solution:    
    # number of ways to solve this 
    # 1. sort the list and create the linkedlist
    # 2. Usual sort on more than 2 sources. 
    #       We maintain the index where the i is smaller and increament it 
    #       ie process next node
    # 3. Merge list 2 at a time and whichever list 
    #       remains at last is your result
    # 4. Use heap for sorting. Aorting while creating the linked list
    #       Now i get it nice approach
    # 5. Divide and conquer basically merge sort 
    #       best approach here.
    def minheap_approach(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minheap = []
        curr = ListNode(0)
        res = curr
        for node_head in lists:
            # put all heads in minheap
            if node_head is not None:
                heapq.heappush(minheap, NodeWrapper(node_head))

        while minheap:
            node_wrapper = heapq.heappop(minheap)
            curr.next = node_wrapper.node
            curr = curr.next

            if node_wrapper.node.next:
                heapq.heappush(minheap, NodeWrapper(node_wrapper.node.next))
        
        return res.next

        


    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        return self.minheap_approach(lists)