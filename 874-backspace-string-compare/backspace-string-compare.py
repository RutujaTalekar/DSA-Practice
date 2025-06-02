class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        def helper(s):
            i = 0
            temp = []
            while i < len(s):
                if s[i].isalpha():
                    temp.append(s[i])
                elif s[i] == '#' and temp:
                    temp.pop()
                i += 1
            return temp
        

        if helper(s) == helper(t):
            return True
        else:
            return False




        

        


        