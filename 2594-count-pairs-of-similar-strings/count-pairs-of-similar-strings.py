class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # O(n)
        seen = {}
        res = 0
        for word in words:
            chars = frozenset(word)
            if chars in seen:
                # This is imp, each new matching set forms a pair with every one of the 
                # already added word sets — resulting in seen[chars] new pairs.
                res += seen[chars]
                seen[chars] += 1
            else:
                seen[chars] = 1

        return res


        # first draft - O(n square)
        '''
         O(n * k) to convert all words into sets.
         O(n * n) for the loop
         comparing sets takes k amount of time, assuming k is number of distinct chars, 
         it can be at most 26 in our case
        '''
        words_set = [set(word) for word in words]
        
        res = 0
        for ws1 in range(0, len(words_set)):
            for ws2 in range(ws1+1, len(words_set)):
                if words_set[ws1] == words_set[ws2]:
                    res += 1
        
        return res


        