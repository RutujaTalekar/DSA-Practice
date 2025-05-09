class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
       
        
        # easy way
        x = str(x)
        rev = x[::-1]
        if rev==x:
            return True
        else :
            return False   


             # one approach
        x = str(x)
        leng = len(x) - 1
        i = 1
        if (x[0] != x[-1]) :
            return False
        while (i < leng//2):
            if x[i] != x[leng - i]:
                return False
            else:
                continue
        return True 