class Solution:
    def countVowelSubstrings(self, word: str) -> int:

        '''
        set = {a,e,i,o,u}
        cuaieuouac
        1 - u
        u+5 check if there are any non vowels
        check if all five vowels are present
        if both true then increase counter
        '''

        i, j = 0, 0
        vowels = {'a','e','i','o','u'}
        result = 0
        for i in range(len(word)-4):
            j = i+4
            while j < len(word):
                window = word[i:j+1]
                if set(window) == vowels:
                    result +=1
                j+=1
        
        return result









        i, j = 0, 0
        vowels = {'a','e','i','o','u'}
        result = 0
        for i in range(len(word)-4):
            substring = ''
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                substring += word[j]
                if len(substring) >= 5 and set(substring) == vowels:
                    result +=1

        return result



            






        