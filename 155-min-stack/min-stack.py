class MinStack:
# or maintain another stack, just keep adding the latest min value in that list and use that.
    def __init__(self):
        self.stack = []
        self.min = math.inf

    def push(self, val: int) -> None:
        self.min = min(self.min, val)
        self.stack.append((val,self.min))
            
    def pop(self) -> None:
        if( self.stack) :
            removed = self.stack[-1]
            del self.stack[-1]
            if(self.stack): 
                top = self.stack[-1]
                self.min = top[1]
            else:
                self.min = math.inf

    def top(self) -> int:
        if(self.stack): 
            top = self.stack[-1]
            return top[0]
        return -1
        

    def getMin(self) -> int:
        if(self.stack): 
            top = self.stack[-1]
            return top[1]
        return -1
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()