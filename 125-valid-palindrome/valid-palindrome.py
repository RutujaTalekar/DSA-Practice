class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_s = ''
        for char in s:
            if char.isalpha():
                clean_s += char.lower()
            if char.isdigit():
                clean_s += char
        
        return clean_s[::-1] == clean_s
        