class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        
        if(n > len(haystack)):
            return -1
        
        for i in range(len(haystack)):
            if (haystack[i:i+n] == needle):
                print('haystack[i:i+n]', haystack[i:i+n] , 'needle[i]', needle)
                return i
        return -1
            
            

