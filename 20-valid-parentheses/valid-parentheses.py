class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')':'(', '}':'{', ']':'['}
        stack = []

        # if len(s) % 2 == 1:
        #     return False

        for char in s:
            if char in lookup:
                if stack and stack[-1] == lookup[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False
            


            
                
                
            
        
        