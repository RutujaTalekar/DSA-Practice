class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonez = sorted(stones, reverse = True)
        # print(stones)
        counter = 0
        if len(stones) == 0:
            return 0
        if len(stones) == 1:
            return stones[0]
        while len(stonez) > 1:
            #Choose 2 heaviest stones
            if(stonez[0] == stonez[1]):
                stonez.pop(0)
                stonez.pop(0)
                stonez.append(0)
            else:
                diff = abs(stonez[0]-stonez[1])
                stonez.pop(0)
                stonez.pop(0)
                stonez.append(diff)
            stonez.sort(reverse = True) 
        return stonez[0]