class TimeMap:

    def __init__(self):
        self.map = {}
        # key -> (timestamp, value)

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.map:
            self.map[key].append((timestamp, value))
        else:
            self.map[key] = [(timestamp, value)]

    def get(self, key: str, timestamp: int) -> str:
        lookup_val = ''

        if key not in self.map:
            return lookup_val

        values = self.map[key]
        # This condition is not needed, 
        # but it helps optimize the performance as this is average case solution
        if values[-1][0] <= timestamp:      
            return values[-1][1]
        
        # binary search - O(logn)
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right) //2
            if values[mid][0] == timestamp:
                return values[mid][1]
            if values[mid][0] < timestamp:
                left = mid + 1
                lookup_val = values[mid][1]
            else:
                right = mid - 1


        # brute force - O(n)
        '''
        for pair in self.cache[key]:
            ts = pair[0]
            if ts <= timestamp:
                lookup_val = pair[1]
        '''
        return lookup_val
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)