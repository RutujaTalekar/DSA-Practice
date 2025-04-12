import math
class Solution(object):
    def isIsomorphic(self, s, t):
        s2t = {}
        t2s = {}
        for ss, tt in zip(s, t):
            if ss not in s2t:
                if tt in t2s:
                    return False
                s2t[ss] = tt
                t2s[tt] = ss
            else:
                if s2t[ss] != tt:
                    return False
        return True
        