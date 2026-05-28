class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity <= 0:
            capacity = 10
        self.capacity = capacity
        self.arr = [0] * capacity
        self.size = 0


    def get(self, i: int) -> int:
        print('get', i)
        if self.arr[i] is None:
            return
        print('return', self.arr[i])
        return self.arr[i]


    def set(self, i: int, n: int) -> None:
        print('set')
        if i > self.capacity:
            return
        self.arr[i] = n
        print('set', self.arr[i])

    def pushback(self, n: int) -> None:
        print('pushback', n)
        if (self.size + 1) > self.capacity:
            self.resize()
        self.arr[self.size] = n
        self.size += 1
        print('size',self.size)
        

    def popback(self) -> int:
        if self.size == 0:
            return
        
        val = self.arr[self.size - 1]
        self.size -= 1
        return val

    def resize(self) -> None:
        new_capacity = self.capacity * 2
        new_arr = [0] * new_capacity
        
        for i in range(len(self.arr)):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
