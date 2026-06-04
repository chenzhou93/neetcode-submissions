class LinkedList:

    class Node:
        def __init__(self, value=None):
            self.value = value
            self.next = None
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    
    def get(self, index: int) -> int:
        if index < 0 or self.head is None:
            return -1
        
        cur = self.head
        cnt = 0

        while cnt < index:
            if cur.next is None:
                return -1
            
            cnt += 1
            cur = cur.next
        
        return cur.value if cur else -1
        
        

    def insertHead(self, val: int) -> None:
        new_node = self.Node(val)
        print('insert head', val)
        
        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
        print('after insert head', self.getValues())
        

    def insertTail(self, val: int) -> None:
        new_node = self.Node(val)
        print('insert tail', val)

        if self.tail is None and self.head is None:
            self.tail = new_node
            self.head = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        
        print('after insert tail', self.getValues())
        
        

    def remove(self, index: int) -> bool:
        print('remove index', index)
        print('removed value', self.get(index))

        if index < 0 or self.head is None:
            return False
        
        if index == 0:
            self.head = self.head.next
            return True
            
        cnt = 0
        cur = self.head

        while cnt < index - 1:
            if cur.next:
                cur = cur.next
                cnt += 1
            else:
                break
        
        if cur.next:
            print('cur value', cur.value)
            if cur.next == self.tail:
                self.tail = cur
            cur.next = cur.next.next
        else:
            return False
        print('after remove 2', self.getValues())
        return True


    def getValues(self) -> List[int]:
        res = []
        cur = self.head
        while cur:
            res.append(cur.value)
            cur = cur.next
        return res
        
