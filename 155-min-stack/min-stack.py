class MinStack(object):

    def __init__(self):
        self.stack = []
        # store the tuples (cur element, min element till now)

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        minimum = val
        
        if self.stack and self.stack[-1][1] < minimum:
            minimum = self.stack[-1][1]
        
        self.stack.append((val, minimum))


    def pop(self):
        """
        :rtype: None
        """
        if self.stack:
            last = self.stack[-1][0]
            self.stack.pop(-1)
            return last
        return -1
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()