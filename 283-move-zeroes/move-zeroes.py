class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        i = 0
        count0 = 0
        while i< n-count0:
            if nums[i] == 0:
                nums.pop(i)
                # nums[i:] = nums[i+1:] This takes more time, pop is better
                nums.append(0)
                count0 += 1
            else:
                i += 1
        return nums
        