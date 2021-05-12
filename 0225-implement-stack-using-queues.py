from collections import deque


class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = deque()
        self.tmp = deque()

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.q.append(x)

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.q) > 1:
            self.tmp.append(self.q.popleft())
        top = self.q.popleft()
        self.q = self.tmp
        self.tmp = deque()
        return top

    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.q) > 1:
            self.tmp.append(self.q.popleft())
        top = self.q.popleft()
        self.q = self.tmp
        self.q.append(top)
        self.tmp = deque()
        return top

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return len(self.q) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
