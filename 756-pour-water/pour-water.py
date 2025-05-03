class Solution(object):
    def pourWater(self, heights, volume, k):
        """
        :type heights: List[int]
        :type volume: int
        :type k: int
        :rtype: List[int]
        """
        '''
        Logic - 
        from the droplet fall index k, 
            go left if left height is lower
            go right if right height is lower
            if both at same level stay there
            break if staying there.
        '''

        n = len(heights)

        # edge cases
        if volume == 0:
            return heights
        
        for _ in range(volume):
            # go left
            idx = k
            lower = k

            while idx - 1 >= 0 and heights[idx-1] <= heights[idx]:
                if heights[idx-1] < heights[idx]:
                    lower = idx -1
                idx -=1

            if lower != k:
                heights[lower] += 1
                continue
            
            # go right
            idx = k

            while idx + 1 < n and heights[idx+1] <= heights[idx]:
                if heights[idx+1] < heights[idx]:
                    lower = idx + 1
                idx +=1

            # if lower != k:
            #     heights[lower] += 1
            #     continue
            # else:
            #     heights[k] += 1

            # instead of writting this I can say

            heights[lower] += 1
        
        return heights
            



            



        
                

            

        