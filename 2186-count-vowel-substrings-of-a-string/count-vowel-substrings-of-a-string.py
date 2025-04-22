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
        vowels = set('aeiou')
        count = 0 
        for i in range(len(word)):
            seen = set()
            for j in range(i, len(word)):
                if word[j] not in vowels:
                    break
                seen.add(word[j])
                if len(seen) == 5:
                    count = count + 1
        return count

        # i, j = 0, 0
        # vowels = {'a','e','i','o','u'}
        # result = 0
        # for i in range(len(word)-4):
        #     j = i+4
        #     while j < len(word):
        #         window = word[i:j+1]
        #         if set(window) == vowels:
        #             result +=1
        #         j+=1
        
        # return result




        