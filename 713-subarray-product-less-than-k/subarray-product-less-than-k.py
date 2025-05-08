class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        '''
        Use a sliding window to maintain a subarray with product less than k. 
        As you expand the window with the right pointer, multiply the current number into the product. 
        If the product becomes >= k, shrink the window from the left. <<<<<<< For each valid window, all 
        subarrays ending at right are valid, so add right - left + 1 to the result. 
        (i.e. num of subarrays made from this window is its length,  This way we dont miss counting 
        the individual elements which are less than k)
        '''

        # sliding window to onvert O(n square) to O(n)
        res = 0
        left = 0
        prod = 1
        for right in range(len(nums)):
            prod *= nums[right]
            # incase invalid prod and decrease the window
            while prod >=k and left <= right:
                prod //= nums[left]
                left += 1

            # incase valid prod, just add to res
            res += (right-left+1)

        return res
        


        # worst case O(n square)
        for i, num in enumerate(nums):
            if num < k:
                res += 1
            prod = num
            idx = i + 1
            while idx < len(nums):
                prod = prod * nums[idx]
                if prod < k:
                    res += 1
                    idx += 1
                else:
                    break
        return res
            


            
            

        