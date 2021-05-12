class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.in_stack = []
        self.out_stack = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.in_stack.append(x)

    def move(self):
        """
        if self.out_stack is empty,
        move elements from in_stack to out_stack
        """
        if not self.out_stack:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.move()
        return self.out_stack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.move()
        return self.out_stack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        self.move()
        return len(self.out_stack) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
