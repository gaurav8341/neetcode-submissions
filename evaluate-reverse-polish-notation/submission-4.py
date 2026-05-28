class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for s in tokens:
            print(s, stack, s.isnumeric())
            
            if s == '+':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a+b))
            elif s == '-':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a-b))
            elif s == '*':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a*b))
            elif s == '/':
                b = stack.pop()
                a = stack.pop()
                stack.append(int(a/b))
            else:
                stack.append(int(s))
                
        return stack.pop()
        