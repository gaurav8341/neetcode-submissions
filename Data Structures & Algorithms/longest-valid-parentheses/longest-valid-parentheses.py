class Solution:
    def longestValidParentheses(self, s: str) -> int:

        stack = [-1] # thi is necessary for case where length = len(s)
        length = 0
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                    # one bracket pair closed
                if stack:
                    length = max(length, i - stack[-1])
                else:
                    stack.append(i)
        return length

        # length = 0
        # # expanding window problem
        # i, j = 0, len(s)-1
        

        # def is_valid():
        #     # O(length(new_s))
        #     stack = []

        #     for idx, c in enumerate(s[a, b]):
        #         if c == '(':
        #             stack.append((c, idx))
        #         elif c == ')':
        #             try:
        #                 stack.pop()
        #             except IndexError:
        #                 return False
            
        #     return len(stack) == 0
        # while j > i:
        #     # but how to decide which pointer to change

        # # for i in range(len(s)):
        # #     for j in range(i+1, len(s)+1):
        # #         new_s = s[i:j]
        # #         if is_valid(new_s):
        # #             length = max(length, len(new_s)) # j -i will also work
        
        # # return length