
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        nums = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        specialNums = {'IV': 4, 'IX': 9, 'XL':40, 'XC':90, 'CD':400, 'CM':900}
        specialChars = ['I','X','C']
        result = 0
        while s:
            char = s[0]
            s = s[1:]
            if char in specialChars and len(s) >= 1:
                nextChar = s[0]
                if char+nextChar in specialNums.keys():
                    s = s[1:]
                    result = result + specialNums[char+nextChar]
                else:
                    result = result + nums[char]
            else:
                result = result + nums[char]
            
        return result
        
'''
        d={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

        sum=0
        for i in range(len(s)):
            if i==len(s)-1:
                sum+=d[s[i]]
            elif d[s[i]]<d[s[i+1]] :
                sum-=d[s[i]]
            else:
                sum+=d[s[i]]
        return sum

'''