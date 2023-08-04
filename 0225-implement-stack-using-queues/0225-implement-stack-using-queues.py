from queue import Queue
class MyStack:

    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def push(self, x: int) -> None:
        # When pushing an element, always enqueue it into q1.
        self.q1.put(x)

    def pop(self) -> int:
        # When popping an element, dequeue all elements from q1 except the last one and enqueue them
        # into q2. Then dequeue the last element from q1 and return it. Swap the names of q1 and q2 to
        # maintain the push operation in q1.
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())
            
        top_element = self.q1.get()
        self.q1, self.q2 = self.q2, self.q1  # Swap the names of q1 and q2
        
        return top_element
       

    def top(self) -> int:
        # The top operation is similar to the pop operation, but instead of dequeuing the last element
        # from q1, return it, without changing the queues.
        while self.q1.qsize() > 1:
            self.q2.put(self.q1.get())

        top_element = self.q1.get()
        self.q2.put(top_element)

        self.q1, self.q2 = self.q2, self.q1  # Swap the names of q1 and q2
        return top_element

    def empty(self) -> bool:
        return self.q1.empty() and self.q2.empty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()