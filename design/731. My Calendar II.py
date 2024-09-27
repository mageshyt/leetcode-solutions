class MyCalendarTwo:

    def __init__(self):
        self.non_overlapping = []
        self.overlapping = []
        

    def book(self, start: int, end: int) -> bool:
        # check if the new event overlaps with any of the overlapping events
        for currStart,currEnd in self.overlapping:
            # if new start is less than the end of the overlapping event and the new end is greater than the start of the overlapping event
            if start<currEnd and end>currStart:
                return False


        # check if the new event overlaps with any of the non-overlapping events
        for currStart,currEnd in self.non_overlapping:
            if start<currEnd and end>currStart:
                # if it overlaps, add the overlapping interval to the overlapping list
                self.overlapping.append((max(start,currStart),min(end,currEnd)))

        # add the new event to the non-overlapping list
        self.non_overlapping.append((start,end))


        return True

                                            
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)
