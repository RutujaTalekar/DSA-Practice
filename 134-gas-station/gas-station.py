class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        '''
        We need cost[i] amount of gas to reach next station (i+1), and at each station 
        we have gas[i] at the station, its easy to visualize if we create a diff array 
        diff[i] = gas[i] - cost[i]
        if diff[i] is -ve then we know that its not possible to reach next station, and 
        this is not viable start position

        A good base case is to know that sum of all gas should be greater than or
        equal to sum of all costs. If this is not true then we can return -1 directly

        This is the greedy approach that works in O(n square) time instead of, having 
        to calculate total starting from each index and checking viable route. 
        If confused check neetcode video.
        '''


        if sum(gas) < sum(cost):
            return -1

        result = 0          # the start index that gives feasible circular route
        total = 0           # use this to add up the diffs 

        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                result = i+1
        
        return result


        