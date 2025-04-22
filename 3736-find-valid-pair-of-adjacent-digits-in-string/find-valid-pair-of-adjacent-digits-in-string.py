class Solution:
    def findValidPair(self, s: str) -> str:

        freq_map = Counter(s)
        i = 0
        while i < len(s)-1:
            if s[i] == str(freq_map[s[i]]) and s[i+1] == str(freq_map[s[i+1]]) and s[i]!=s[i+1]:
                return s[i]+s[i+1]
            
            i+=1
        
        return ''



        