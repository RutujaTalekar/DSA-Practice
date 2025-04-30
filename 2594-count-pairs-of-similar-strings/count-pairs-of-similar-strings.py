class Solution:
    def similarPairs(self, words: List[str]) -> int:
        words_set = [set(word) for word in words]
        
        res = 0
        for ws1 in range(0, len(words_set)):
            for ws2 in range(ws1+1, len(words_set)):
                if words_set[ws1] == words_set[ws2]:
                    res += 1
        
        return res


        