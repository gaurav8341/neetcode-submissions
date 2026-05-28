class Solution:
    def isValid(self, s: str) -> bool:
        brack_dict = {']': '[', '}':'{', ')':'('}
        brack_stack = []

        for c in s:
            if c in brack_dict.values():
                brack_stack.append(c)
            if c in brack_dict.keys():
                if len(brack_stack) > 0 and brack_stack[-1] == brack_dict[c]:
                    brack_stack.pop()
                else:
                    return False
        
        if len(brack_stack) == 0:
            return True
        
        return False