class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        '''
        Play with indices to get zig zag pattern
        First char -> char at 0, place in op
        next char -> + (numRows + 2), and so on for first row
        second row first char - > char at 1
        next char -> i+ 4 and then i + 6 so on
        third row -> i+ 2 and then i + 6 so on
        '''

        if len(s)<= 1 or numRows == 1:
            return s

        res = ''
        
        for row in range(numRows):
            step = (numRows-1) * 2
            for i in range(row, len(s), step):
                res += s[i]
                next_char = i + (step - 2*row)
                if not( row == 0 or row == numRows - 1 ) and next_char < len(s):
                    '''
                    1 -> 4th    (step - 2* (1))
                    2 -> 2nd    (step - 2* (2))
                    '''
                    res += s[next_char]
        
        return res
                


        