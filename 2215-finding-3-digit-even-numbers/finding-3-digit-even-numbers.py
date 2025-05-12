class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        '''
        100 - 999
        Check every num in this range and see if it can be formed with given integers
        '''

        output = []

        def helper(target):
            freq = Counter(digits)
            target_str = list(str(target))

            
            while target_str:
                digit = int(target_str.pop())

                if digit not in freq:
                    return False
                if digit in freq and freq[digit] == 0:
                    return False

                freq[digit] -= 1
            
            output.append(target)
            return True

        
        for target in range(100, 1000, 2):
            helper(target)
        
        return output

            



        
        