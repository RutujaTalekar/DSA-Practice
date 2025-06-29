class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binSearch(nums, target, lrFlag):
            left, right = 0, len(nums)-1
            index = -1
            while left<= right:
                mid = (left+right) // 2
                if target < nums[mid]:
                    right = mid - 1
                elif target > nums[mid]:
                    left = mid + 1
                else:
                    index = mid
                    if lrFlag: # if true -> we are looking for left index
                        right = mid - 1
                    else:
                        left = mid + 1
            return index
        
        return [binSearch(nums, target, True), binSearch(nums, target, False)]

    
    #     left = self.binSearch(nums, target, True)
    #     right = self.binSearch(nums, target, False)
    #     return [left, right]
    # def binSearch(self, nums, target, leftBiased):
    #         l,r = 0, len(nums)-1
    #         i = -1
    #         while l<=r:
    #             m = (l+r)//2
    #             if target > nums[m]:
    #                 l = m + 1
    #             elif target < nums[m]:
    #                 r = m - 1
    #             else:
    #                 i = m
    #                 if leftBiased:
    #                     r = m-1
    #                 else:
    #                     l = m+1
    #         return i

        
