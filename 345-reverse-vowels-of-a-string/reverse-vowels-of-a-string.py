class Solution:
    def reverseVowels(self, s: str) -> str:

        result = list(s)
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s)-1
        
        while left < right:
            if s[left] not in vowels:
                left += 1

            elif s[right] not in vowels:
                right -=1
                
            else:
                result[left], result[right] = result[right], result[left]
                left += 1
                right -= 1

        return ''.join(result)
        