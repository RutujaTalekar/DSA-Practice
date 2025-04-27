class TimeMap(object):

    def __init__(self):
        self.cache = {}
        # key -> [(timestamp, value)...]

    def set(self, key, value, timestamp):
        """
        :type key: str
        :type value: str
        :type timestamp: int
        :rtype: None
        """
        if key not in self.cache:
            self.cache[key] = []
        self.cache[key].append((timestamp, value))

    def get(self, key, timestamp):
        """
        :type key: str
        :type timestamp: int
        :rtype: str
        """
        lookup_val = ''
        if key not in self.cache:
            return lookup_val
        
        # binary search - O(logn)
        values = self.cache[key]
        left, right = 0, len(values)-1
        while left <= right:
            mid = (left + right) //2
            if values[mid][0] <= timestamp:
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