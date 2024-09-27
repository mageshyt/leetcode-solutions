
class Tree:
    def __init__(self,start ,end):
        self.left= None
        self.right= None
        self.start= start
        self.end= end
    def insert(self, start, end):
        current= self
        while True:
            if start >= current.end:
                if not current.right:
                    current.right= Tree(start,end)
                    return True
                current= current.right
            elif end <= current.start:
                if not current.left:
                    current.left= Tree(start,end)
                    return True
                current= current.left

            else:
                return False

            
class MyCalendar:

    def __init__(self):
        self.events= []
        self.root= None
        

    def book(self, start: int, end: int) -> bool:
        # if the events list is empty, add the event
        if not self.events:
            self.events.append((start,end))
            return True

        for _start, _end in self.events:
            if start < _end and end > _start:
                return False

        self.events.append((start,end))

        return True 
    def bookTree(self,start:int,end:int)->bool:
        if not self.root:
            self.root= Tree(start,end)
            return True


        return self.root.insert(start,end)

# Time complexity: O(N^2)
# Space complexity : O(N)


