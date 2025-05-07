class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        mid= 0
        while (left <= right):
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]:
                # if it is i.e. left side is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1 
                else :
                    left = mid + 1
            else:
                # if not that means right is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid -1

        return -1

        



        