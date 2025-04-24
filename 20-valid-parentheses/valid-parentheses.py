class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {')':'(', '}':'{', ']':'['}
        stack = []

        for char in s:
            if char in lookup:
                if stack and stack[-1] == lookup[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        
        return True if not stack else False


        
        map = { ')':'(' , '}':'{' , ']':'['  }
        stack = []

        for key in s:
            if key in map.values():
                stack.append(key)

            else:
                if stack:
                    if stack[-1]!= map[key]:
                        return False
                    stack.pop() #matching pair\
                else:
                    return False

        return True if not stack else False
        
            


            
                
                
            
        
        