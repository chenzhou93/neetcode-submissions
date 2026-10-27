class Node:
    def __init__(self, key=None, data=None):
        self.data = data
        self.key = key
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        
        

    def get(self, key: int) -> int:
        val = -1
        if key in self.cache:
            node = self.cache[key]
            val = node.data
            self.remove(node)
            self.add(node)
        return val
        

    def put(self, key: int, value: int) -> None:
        node = None
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        else:
            node = Node()
            if len(self.cache) == self.capacity:
                removal_key = self.head.next.key
                self.remove(self.head.next)
                del self.cache[removal_key]
        
        node.data = value
        node.key = key
        self.cache[key] = node

        self.add(node)

    
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
    
    def add(self, node):
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node


        
