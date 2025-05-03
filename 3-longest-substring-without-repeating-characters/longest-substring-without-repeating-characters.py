class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        Use sliding window pointers - prev, cur to keep track of substring
        Use sets to keep track of unique characters from substring
        '''

        unique = set()
        res = 0
        cur = 0
        prev = cur
        while cur < len(s):
            
            while s[cur] in unique:
                unique.remove(s[prev])
                prev += 1

            unique.add(s[cur])
            res = max(res, len(unique))
            
            cur += 1
            
        return res

        

            




            