class Solution:
    def decodeString(self, s: str) -> str:
        '''
        Intuition explained in book notes
        Time complexity - O(n+m), n -> len of s, m -> total len of decoded string (all chars)
        We do O(n) work to read and process each character using a stack, 
        and O(m) work to build the full decoded result. 
        So the total time depends on both the size of the input and how many characters the decoded string contains.
        '''
        stack = []
        i = 0
        for i in range(len(s)):
            if s[i] != ']':
                stack.append(s[i])
                i += 1
            else:
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
        
        return ''.join(stack)

            


            

