class BrowserHistory:

    class Node:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, homepage: str):   
        home_page_node = self.Node(homepage)
        self.pointer = home_page_node
        

    def visit(self, url: str) -> None:
        if url == "":
            return
        
        new_web = self.Node(url)

        self.pointer.next = new_web
        new_web.prev = self.pointer
        self.pointer = new_web

        

    def back(self, steps: int) -> str:
        if steps < 0:
            return

        cur = self.pointer

        while cur.prev and steps > 0:
            cur = cur.prev
            steps -= 1
        
        self.pointer = cur

        return cur.val
        

        

    def forward(self, steps: int) -> str:
        if steps < 0:
            return
        
        cur = self.pointer

        while cur.next and steps > 0:
            cur = cur.next
            steps -= 1
        
        self.pointer = cur

        return cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)