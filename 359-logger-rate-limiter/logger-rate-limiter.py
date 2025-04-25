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
        
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)