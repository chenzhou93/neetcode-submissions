class MyLinkedList:

    class Node:
        def __init__(self, val):
            self.prev = None
            self.next = None
            self.val = val

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0:
            return -1
        
        cur = self.head
        cnt = 0

        while cur:
            if cnt == index:
                return cur.val
            cur = cur.next
            cnt += 1
        
        return -1

    def addAtHead(self, val: int) -> None:
        if self.head is None:
            self.head = self.Node(val)
            self.tail = self.head
            self.size += 1
            return
        
        node = self.Node(val)
        node.next = self.head
        self.head.prev = node
        self.head = node
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        if self.tail is None:
            self.head = self.Node(val)
            self.tail = self.head
            self.size += 1
            return
        
        node = self.Node(val)

        if self.tail:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            
            cur.next = node
            node.prev = cur
            self.tail = cur
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            node = self._findAtIndex(index)
            print('node.val',node.val)

            if node is not None:
                new_node = self.Node(val)
                new_node.next = node
                new_node.prev = node.prev
                node.prev.next = new_node
                node.prev = new_node
                self.size += 1
        

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        
        node = self._findAtIndex(index)
        
        if node:
            prev = node.prev
            next = node.next

            if prev:
                prev.next = next
            else:
                self.head = next
            
            if next:
                next.prev = prev
            else:
                self.tail = prev
            
            self.size -= 1
        
    
    def _findAtIndex(self, index) -> Node:      
        cur = self.head
        cnt = 0

        while cur:
            print('cnt', cnt)
            if cnt == index:
                print(f'{cnt} == {index}')
                return cur
            cur = cur.next
            cnt += 1
        
        return None
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)