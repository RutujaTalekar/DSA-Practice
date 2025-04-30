class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def getMaxNumList(nums, k):
            stack = []
            to_remove = len(nums) - k

            for num in nums:
                while stack and to_remove > 0 and stack[-1] < num:
                    stack.pop()
                    to_remove -= 1
                stack.append(num)
            
            return stack[:k]
        
        def merge(nums1, nums2):
            # Merge greedily, dont just use extend method
            result = []
            while nums1 or nums2:
                # Compare lexicographically which list is larger
                if nums1 > nums2:
                    result.append(nums1.pop(0))
                else:
                    result.append(nums2.pop(0))
            return result



        res = []
        output = []
        for i in range(0, k+1):     # stop index is K+1 and not K since we have to consider a partition where i = 2 as well           
            if i <= len(nums1) and (k-i)<= len(nums2):  # Important for efficiency
                res = merge(getMaxNumList(nums1, i), getMaxNumList(nums2, k-i))
                output = max(output, res)

        
        # print(output)
        return output
        
