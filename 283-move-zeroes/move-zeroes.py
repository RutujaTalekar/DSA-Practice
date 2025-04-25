class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # neetcode way, takes less space
        l, r= 0, 0
        for r in range(len(nums)):
            if nums[r] != 0:
                nums[l], nums[r] = nums[r], nums[l]
                l+=1
        return nums

        # more intuitive way
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
        