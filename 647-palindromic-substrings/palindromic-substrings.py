class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        res = n

        # maintain an axis and look for chars both ways using 2 pointers - to check palindrom

        for i, char in enumerate(s):
            # check odd palindromes
            left, right = i-1, i+1
            while left >= 0 and right < n and s[left] == s[right]:
                res +=1
                left -= 1
                right += 1
            
            # check even palindromes
            left, right = i-1, i
            while left >= 0 and right < n and s[left] == s[right]:
                res +=1
                left -= 1
                right += 1
        
        return res
            



