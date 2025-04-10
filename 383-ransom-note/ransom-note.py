class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        #Brute Force
        '''
        iterate over ransom Note
        check if each letter exists in magzine
        the second step will be O(n) in brute force but if we use 
        hashmap, the lookup will be O(1)
        '''

        lookup = defaultdict(int)
        for char in magazine:
            lookup[char]+=1

        # print(lookup)
        
        for char in ransomNote:
            if char in lookup and lookup[char] != 0:
                lookup[char] -=1
            else:
                return False
        
        
        return True

   

        