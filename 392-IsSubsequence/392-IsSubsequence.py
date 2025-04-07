# Last updated: 4/7/2025, 6:16:35 PM
class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(t)<len(s):
            return False
        
        l=0

        for r in range(len(t)):
            if l == len(s):
                return True

            if s[l] == t[r]:
                l+=1
        
        return l==len(s)