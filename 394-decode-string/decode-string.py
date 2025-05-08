class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            while i < len(s) and s[i] != ']':
                stack.append(s[i])
                i += 1

            
            if i < len(s):
                chars = ''
                while stack and stack[-1] != '[':
                    char = stack.pop(-1)
                    chars = char + chars
                
                stack.pop(-1) # remove the opening bracket

                k = ''
                while stack and stack[-1].isdigit():
                    num = stack.pop(-1)
                    k = num + k
                
                substring = int(k) * chars
                stack.append(substring)
                i += 1
        
        return ''.join(stack)

            


            

