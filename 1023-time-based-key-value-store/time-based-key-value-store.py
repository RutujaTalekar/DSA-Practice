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
        # Instead of brute force we can do the search with binary search
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left+right)//2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif timestamp > values[mid][0]:
                left = mid + 1
                lookup_val = values[mid][1]
            else:
                right = mid - 1
        
        # This is fair approach but it gives TLE
        '''
        for ts, val in values:
            if ts <= timestamp:
                lookup_val = val
        '''
        
        return lookup_val
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)