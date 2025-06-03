class Solution:

    def backspaceCompare(self, s: str, t: str) -> bool:

        # Medium solution with time - O(m+n) and memory O(1)
        
        def validChar(str, idx):
            backspace = 0
            while idx >= 0:
                if str[idx] == '#':
                    backspace += 1
                elif backspace > 0 :
                    backspace -= 1
                else:
                    return idx
                idx -= 1
            return -1
        
        # our helper function should return the valid characters from each 
        # string so we can go ahead and compare them in another loop, which saves memory 
        len_s, len_t = len(s)-1, len(t)-1
        while len_s >= 0 or len_t >= 0:
            idx_s = validChar(s, len_s)
            idx_t = validChar(t, len_t)

            # indexes can be out of bounds
            char_s = s[idx_s] if idx_s >= 0 else ''
            char_t = t[idx_t] if idx_t >= 0 else ''

            if char_s != char_t:
                return False
                
            # reposition the counters to find next valid char after the current valid char
            len_s = idx_s -1
            len_t = idx_t -1

        # if all characters matched, then we reach at the final return. 
        return True



        # Easy solution with time - O(m+n) and memory O(m+n)
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
        




        

        


        