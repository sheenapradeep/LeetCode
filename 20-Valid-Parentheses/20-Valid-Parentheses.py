# Runtime: 52ms (42.67%) Memory Usage: 13.9 MB (26.48%) 
class Solution:
    def isValid(self, s: str) -> bool:
       ## Checks to see if string length is odd 
        if not(len(s)%2 == 0):
            return False
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            else:
                if len(stack)> 0:
                    checkval = stack.pop()
                    if not(checkval == '(' and i == ')') and not(checkval == '{' and i == '}') and not(checkval == '[' and i == ']'):
                        return False
                elif len(stack) == 0:
                    return False
        return len(stack) == 0
    
