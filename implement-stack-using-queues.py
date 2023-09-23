from collections import deque


class MyStack:
    def __init__(self):
        self.queue1 = deque()  # Main queue
        self.queue2 = deque()  # Temporary queue for operations

    def push(self, x: int) -> None:
        # Push the element onto the empty queue (either queue1 or queue2)
        if not self.queue1:
            self.queue1.append(x)
            while self.queue2:
                self.queue1.append(self.queue2.popleft())
        else:
            self.queue2.append(x)
            while self.queue1:
                self.queue2.append(self.queue1.popleft())

    def pop(self) -> int:
        if self.queue1:
            return self.queue1.popleft()
        elif self.queue2:
            return self.queue2.popleft()
        else:
            return None  # Stack is empty

    def top(self) -> int:
        if self.queue1:
            return self.queue1[0]
        elif self.queue2:
            return self.queue2[0]
        else:
            return None  # Stack is empty

    def empty(self) -> bool:
        return not self.queue1 and not self.queue2


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
