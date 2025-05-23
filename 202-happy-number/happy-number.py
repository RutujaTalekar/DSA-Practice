class Solution:
    def isHappy(self, n: int) -> bool:
        
        digSquareSum = 0
        remember = {}

        # while (len(str(n)) != 1): # this fails when given n is single digit example n = 7, expected True
        while(n not in remember):
            key = n

            while(n != 0):
                digit = n%10 
                n = n//10 
                digSquareSum += digit**2 
            
            n = digSquareSum
            remember[key] = digSquareSum
            digSquareSum = 0
            
        if n == 1:
            return True
        else:
            return False  


        '''
        Algorithm with HashMap
        {
            19: 82
            82: 68
            68: 100
            100: 1
        }

        {
            7:49
            49: 16+81
            97: 81+49
            130: 19
            10: 1
        }

        {
            2: 4
            4: 16
            16: 37
            37: 9+ 49
            58: 25 + 64
            89: 64+81
            145: 1+16+25
            42: 16+ 4
            20: 4
            4
        }

        {4,}

        '''
                  






        