class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = [str(digit) for digit in digits]
        num = ''.join(digits)
        res = int(num) + 1

        digits = [int(digit) for digit in str(res)]

        return digits
        