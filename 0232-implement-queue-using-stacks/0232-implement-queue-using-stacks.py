class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        # When pushing an element, always push it onto s1
        self.s1.append(x)

    def pop(self) -> int:
        # When performing a pop or peek operation, transfer all elements from s1 to s2, which will
        # reverse their order.
        
        if not self.s2: # note: append to s2 only when it is empty 
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2.pop()

    def peek(self) -> int:
        # For the peek operation, peek at the top element of s2 without removing it.
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())
        
        return self.s2[-1]

    def empty(self) -> bool:
        return not self.s1 and not self.s2


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()