class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if self.cache and key in self.cache:
            node = self.cache[key]
            value = node.val
            self._remove(node)
            self._add(node)
            return value
        return -1

    def _add(self, new_node) -> None:
        # head <-> node1 <-> tail
        # head <-> new node <-> node1 <-> tail
        next_node = self.head.next
        self.head.next = new_node
        new_node.prev = self.head
        new_node.next = next_node
        next_node.prev = new_node
    
    def _remove(self, old_node) -> None:
        # head <-> old node <-> node1 <-> tail
        # head <-> node1 <-> tail
        next_node = old_node.next
        prev_node = old_node.prev
        prev_node.next = next_node
        next_node.prev = prev_node


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)
        
        new_node = Node(key,value)
        self._add(new_node)
        self.cache[key] = new_node

        if len(self.cache) > self.capacity:
            node = self.tail.prev
            self._remove(node)
            del self.cache[node.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)