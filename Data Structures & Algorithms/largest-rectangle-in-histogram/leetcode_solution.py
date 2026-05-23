class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # stack 
        stack = []
        max_area = 0

        # to find area of recatngle weill need both length and height
        # index here will help in getting length
        for i, h in enumerate(heights):
            # start in case of backward length will need start
            start = i
            # if current height is less than top of stack.
            # we wont be needing top stack element.
            while stack and stack[-1][1] > h:
                idx, ht = stack.pop()
                
                # get the area
                max_area=max(max_area, (i-idx)*ht)
                # get the index until which the current element i,h
                # can be extended in past eleents
                start = idx
            # append past extend index and height of current element 
            stack.append((start, h))
        
        # After all this the stack may not be empty
        for i,h in stack:
            # get the area here the height will be h and 
            # length will be from last index of heights array 
            # to the start element of the height h
            max_area=max(max_area, (len(heights) - i) * h)

        return max_area

