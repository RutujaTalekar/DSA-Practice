class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        '''
        check len(needle) <= len(haystack)
        '''
        need_len, hay_len = len(needle), len(haystack)

        if need_len > hay_len:
            return -1
        
        if need_len == hay_len and haystack == needle:
            return 0
        
        for i in range(0, hay_len - need_len + 1):
            res = i
            idx = 0
            
            while idx < need_len and haystack[i] == needle[idx]:
                i += 1
                idx += 1
            
            if idx == need_len:
                return res
            
        return -1
            
            

