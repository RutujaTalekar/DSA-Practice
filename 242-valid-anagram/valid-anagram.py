class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        # base case for any solution
        if len(s) != len(t):
            return False
        
        # another solution with Counter maps
        s_map = Counter(s)
        t_map = Counter(t)
        return s_map == t_map
        
        # another solution with sets
        for cha in set(s): 
            if s.count(cha)!=t.count(cha):
                return False
        return True
        
        # draft 1 solution
        s_map = Counter(s)

        for char in t:
            if s_map[char] and s_map[char] > 0:
                s_map[char] -=1
            else:
                return False
        
        return 0 == sum(s_map.values())
        
        