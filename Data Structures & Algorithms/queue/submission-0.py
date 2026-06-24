class Deque:
    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None
    
    def __init__(self):
        self.size = 0
        self.head = self.tail = None


    def isEmpty(self) -> bool:
        return self.size == 0
        

    def append(self, value: int) -> None:
        node = self.Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        
        self.size += 1
        

    def appendleft(self, value: int) -> None:
        node = self.Node(value)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        
        self.size += 1
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        res = self.tail.val

        if self.tail.prev:
            self.tail = self.tail.prev

        self.size -= 1

        return res;
        

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        res = self.head.val

        if self.head.next:
            self.head = self.head.next

        self.size -= 1

        return res;
        
