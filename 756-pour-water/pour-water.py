class Solution:
    def pourWater(self, heights: List[int], volume: int, k: int) -> List[int]:
        '''
        Intuition - 
        from the droplet fall index k, 
            go left if left height is lower
            go right if right height is lower
            if both at same level stay there
            break if staying there.
        '''

        '''
        IMP part of logic - 
        If left is lower (<) - update best and move 
        If left is same (==) just move, but don't update best. Keep moving cause there might be a lower value ahead.
        If left is higher (>) stop moving 
        Same applied for right movement
        '''

        # edge cases
        if k > len(heights):
            return -1
        if len(heights) == 1:
            return [heights[0] + volume]
        

        for _ in range(volume):
            best = idx = k

            # check left
            while idx-1 >= 0 and heights[idx-1] <= heights[idx]:
                if heights[idx-1] < heights[idx]:
                    best = (idx-1)
                idx -= 1

            # if we found a lower position on left, we can continue with next drop
            if best != k: 
                heights[best] += 1
                continue
            
            best = idx = k
            # if not found on left, check right
            while idx+1 < len(heights) and heights[idx+1] <= heights[idx]:
                if heights[idx+1] < heights[idx]:
                    best = (idx +1)
                idx += 1
            
            # if we found lower position on right, it will be in best, or else best will be the k position
            heights[best] += 1

        return heights


            

        