class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ''
        step = 0

        if numRows == 1 or len(s) == 1:
            return s

        for row in range(numRows):
            step = 2*(numRows-1)
            for i in range(row, len(s), step):
                res += s[i]
                also_include_char_at = i + (step - 2*(row))
                if not(row == 0 or row == numRows-1) and also_include_char_at < len(s):
                    res += s[also_include_char_at]  
        
        return res
