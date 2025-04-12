class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # simple approach with O(n) time and space
        '''
        nums_map = Counter(nums)

        for num, count in nums_map.items():
            if count > len(nums)/2:
                return num
        '''

        # Boyer-Moore Voting Algorithm
        # O(n) time O(1) space
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


            



        
        