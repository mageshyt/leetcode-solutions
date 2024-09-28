class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = []
        self.k = k
        

    def insertFront(self, value: int) -> bool:
        # if the queue is full, return False
        if len(self.queue) == self.k:
            return False
        # insert the value at the front of the queue
        self.queue.insert(0,value)
        return True

        

    def insertLast(self, value: int) -> bool:
        # if the queue is full, return False
        if len(self.queue) == self.k:
            return False
        # insert the value at the end of the queue
        self.queue.append(value)
        return True


        

    def deleteFront(self) -> bool:
        # if the queue is empty, return False
        if len(self.queue) == 0:
            return False
        # remove the first element from the queue
        self.queue.pop(0)

        return True
        

    def deleteLast(self) -> bool:
        # if the queue is empty, return False
        if len(self.queue) == 0:
            return False
        # remove the last element from the queue
        self.queue.pop()
        return True
        

    def getFront(self) -> int:
        # if the queue is empty, return -1
        if len(self.queue) == 0:
            return -1
        # return the first element of the queue
        return self.queue[0]
        

    def getRear(self) -> int:
        # if the queue is empty, return -1
        if len(self.queue) == 0:
            return -1
        # return the last element of the queue
        return self.queue[-1]
        

    def isEmpty(self) -> bool:
        # if the queue is empty, return True
        return len(self.queue) == 0
        

    def isFull(self) -> bool:
        # if the queue is full, return True
        return len(self.queue) == self.k
        

