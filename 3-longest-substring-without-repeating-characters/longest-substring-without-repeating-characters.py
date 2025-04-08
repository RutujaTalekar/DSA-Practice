class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        set_s = set(s)
        temp = set()

        if len(set_s) == len(s):
            return len(set_s)
        # a b c a b c b b
        # 0 1 2 3 4 5 6 7
        # cur = 3
        # prev = 0

        result = 0
        cur, prev = 0, 0
        while cur < len(s):
            while s[cur] in temp:
                result = max(result, len(temp))
                temp.remove(s[prev])
                prev += 1
                
            temp.add(s[cur])
            cur += 1
        
        result = max(result, len(temp))
        
        return result
                





        



        
        return 0
        

        






        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # characterSet = set()
        # result = 0
        # l = 0
        # for r in range(len(s)):
        #     while s[r] in characterSet:
        #         characterSet.remove(s[l])
        #         l+=1
        #     characterSet.add(s[r])
        #     result = max(result, r-l+1)
        # return result
        

