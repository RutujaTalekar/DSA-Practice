class RandomizedSet:
    # Read the intuition from book notes. Its easy after that.

    def __init__(self):
        self.map = {} # Stores val -> idx
        self.list = [] # Stores all vals, so we can get indices to feed into get random function

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        else:
            self.map[val] = len(self.list)  # will give current index of the recently adding element
            self.list.append(val)           # now also append to list
            return True


    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        else:
            old_idx = self.map[val]     
            last_val = self.list[-1]    # get last val from list, to put in old_idx O(1), 
                                        # instead of restructuring the entire list in O(n)
                                        # dont pop it yet, just in case the val to remove == last_val 
                                        # it will cause error
                                        
            self.list[old_idx] = last_val 
            self.map[last_val] = old_idx    # update the index in hashmap as well
            self.list.pop()                 # remove last val from list, cause its present at old_idx
            del self.map[val]               # delete the val from hashmap                                

            return True
            

    def getRandom(self) -> int:
        rand_idx = random.randint(0, len(self.list) - 1)
        return self.list[rand_idx]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()