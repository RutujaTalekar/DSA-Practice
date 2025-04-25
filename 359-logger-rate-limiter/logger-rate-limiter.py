class Logger:

    def __init__(self):
        self.tracker = {}
        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.tracker:
            self.tracker[message] = timestamp
            return True
        else:
            old_time = self.tracker[message]
            if timestamp - old_time >= 10:
                self.tracker[message] = timestamp
                return True
        return False

    # Can be implemented using set and pq
    '''
    def __init__(self):
        self.hash_set = set() # message
        self.dq = deque() # (timestamp, message)

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        while self.dq and (timestamp - self.dq[0][0] >= 10):
            self.hash_set.remove(self.dq[0][1])
            self.dq.popleft()
        
        if message in self.hash_set: return False
        self.dq.append((timestamp, message))
        self.hash_set.add(message)
        return True
    '''
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)