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
        # sliding window pointers
        i, j = 0, 0
        vowels = {'a','e','i','o','u'}
        result = 0
        
        for i in range(len(word)-4):
            j = i+4
            while j < len(word) and word[j] in vowels:
                window = word[i:j+1]
                if set(window) == vowels:
                    result +=1
                j+=1
        
        return result

        # lookup = {idx:char for idx,char in enumerate(word)}
        # a e i o u u
        # 0 1 2 3 4 5
            






        