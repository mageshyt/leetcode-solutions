import collections

class MyStack:
    def __init__(self):
        # Initialize an empty list to simulate the stack.
        self.queue = []

    def push(self, x: int) -> None:
        # Add the new element to the end of the queue.
        self.queue.append(x)
        
        # Move all elements except the newly added one to the end of the queue.
        for _ in range(len(self.queue) - 1):
            self.queue.append(self.queue.pop(0))

    def pop(self) -> int:
        # Remove and return the front element of the queue (which is the top of the stack).
        return self.queue.pop(0)

    def top(self) -> int:
        # Return the last element of the queue (which is the top of the stack).
        return self.queue[0]

    def empty(self) -> bool:
        # Check if the queue is empty.
        return len(self.queue) == 0
