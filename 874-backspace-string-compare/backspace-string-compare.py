class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:

        def helper_optimized(s):
            i = len(s)
            skip = 0
            temp = []
            while i >= 0:
                if s[i] == '#':
                    skip += 1
                elif skip > 0:
                    skip -=1
                    i -= 1
                else:
                    temp.append(s[i])
                    
                    
                
                i -= 1

            print(temp, i) 

            





        
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
        




        

        


        