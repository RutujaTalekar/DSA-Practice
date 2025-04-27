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
        # edge cases
        if k >= len(heights):
            return -1
        if len(heights) == 1:
            return [heights[0] + volume]

        for _ in range(volume):
            idx = k

            # move left
            best = k
            while idx - 1 >= 0 and heights[idx-1] <= heights[idx]:
                if heights[idx-1] < heights[idx]:
                    best = idx-1
                idx -= 1

            if best != k:
                heights[best] += 1
                continue

            # move right
            idx = k
            best = k
            while idx + 1 < len(heights) and heights[idx+1] <= heights[idx]:
                if heights[idx+1] < heights[idx]:
                    best = idx+1
                idx += 1

            if best != k:
                heights[best] += 1
                continue

            # stay
            heights[k] += 1

        return heights



            
            

                

            

        