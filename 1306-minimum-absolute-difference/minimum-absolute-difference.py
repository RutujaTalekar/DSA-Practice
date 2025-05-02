class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:

        '''
        Brute force - run two loops with i = 0 -> n-1 and j = i+1 -> n 
        and store the diff in hasmap as key with the values. And then
        sort and return the min diff list. N square solution with added space

        Better approach - sort the array, and then check only consequent diffs
        store them in hashmap - key is index and val is diff
        Then for the min value, and create list of list
        '''
        map_result = defaultdict(list)
        minimum = abs(arr[0] - arr[1])  #we will have minimum 2 elements in arr
        arr.sort()
        for i in range(len(arr)-1):
            diff = abs(arr[i]-arr[i+1])
            if diff <= minimum :
                minimum = diff
                map_result[diff].append([arr[i], arr[i+1]])

        minimum = min(map_result.keys()) 
        
        return map_result[minimum]