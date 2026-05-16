class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        last_elem = None
        # use stack 
        # in stack the latest element 
        # should be smaller than its below element

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                ans_i, ans_t = stack.pop()
                
                result[ans_i] = i - ans_i
                
            stack.append((i, t))
        
        return result

