class Solution:
    def findValidPair(self, s: str) -> str:

        freq_map = Counter(s)

        for i in range(len(s)-1):
            a, b = s[i], s[i + 1]
            if a != b and a == str(freq_map[a]) and b == str(freq_map[b]):
                return a+b
        return ''



        