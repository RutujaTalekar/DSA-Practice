class Solution:
    def longestPalindrome(self, s: str) -> str:
        '''
        Intuition - instead of checking from the left and right bounds of substring to
        confirm the nature of palindrome, treat each character as middle element and 
        check if the left and right neighbors of it are equal, and keep expanding the 
        bounds. This gives odd palindromes, what about even?

        '''
        res = ''

        for i, char in enumerate(s):

            # odd palindromes
            left = right = i
            while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > len(res):
                        res = s[left:right+1]
                    left -= 1
                    right += 1
            
            # even palindromes
            left, right = i, i + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if right - left + 1 > len(res):
                        res = s[left:right+1]
                left -= 1
                right += 1

        

        return res




  
