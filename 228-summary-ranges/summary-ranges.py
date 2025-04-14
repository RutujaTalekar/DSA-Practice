class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        '''
        nums -> first element 0 last element 7 <- This is range
        traverse between 0 to 7
        remember start of the range and cur element, 
        populate the output when elment from range is missing in nums
        '''

        output = []
        if not nums:
            return output
        if len(nums) < 2:
            return [str(num) for num in nums]


        cur = nums[0]
        last = nums[-1]
        total = len(nums)
        idx = 0

        while(idx < total):
            start = end = cur 

            while (cur in nums):
                end = cur 
                cur +=1
                idx += 1
            
            if start!= end:
                output.append(str(start)+'->'+str(end))
            elif (end in nums):
                output.append(str(start))
            else:
                pass


            if idx < total:
                cur = nums[idx]
            else:
                break
            
        
        return output







        