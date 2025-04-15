class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        Edge cases - 
        if len(needle) > len(haystack), invalid
        if len of both is same then check directly and return result
        '''
        need_len, hay_len = len(needle), len(haystack)

        if need_len > hay_len:
            return -1

        for i in range(0, hay_len - need_len + 1):
            res = i
            idx = 0

            while idx < need_len and haystack[i] == needle[idx]:
                i += 1
                idx += 1
            
            if idx == need_len:
                return res
            
        return -1
            
            

