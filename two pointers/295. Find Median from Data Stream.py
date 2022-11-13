'''The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.


Example 1:

Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
'''

class solution:
    def __init__(self):
        self.small_heap = []  # here we use min head
        self.large_heap = []  # here we use max head

    def addNum(self, num: int) -> None:
        # first always add to the small heap
        heapq.heappush(self.small_heap, -1*num)

      # first make sure all the elements in the small heap are smaller than the large heap
        small_val = -1*self.small_heap[0]
        large_val = self.large_heap[0] if self.large_heap else 0
        if(self.small_heap and self.large_heap and small_val > large_val):
            # then pop the smallest element from the small heap and add it to the large heap
            small_val = -1*heapq.heappop(self.small_heap)
            # add the small value to the large heap
            heapq.heappush(self.large_heap, small_val)

        # for not equal size
        # first for the small heap > large
        if(len(self.small_heap) > len(self.large_heap)+1):
          # pop form small heap and add to large heap
            small_val = -1*heapq.heappop(self.small_heap)
            heapq.heappush(self.large_heap, small_val)
        # second for small heap < large
        if(len(self.small_heap) < len(self.large_heap)):
            large_val = heapq.heappop(self.large_heap)  # take from large
            heapq.heappush(self.small_heap, -1*large_val)  # add to small

        return None

    def findMedian(self) -> float:
        median: float = 0.0
        if(len(self.small_heap) == len(self.large_heap)):
            median = (-1*self.small_heap[0]+self.large_heap[0])/2
        elif (len(self.small_heap) > len(self.large_heap)):
            median = -1*self.small_heap[0]
        else:
            median = self.large_heap[0]

        return median


if __name__ == '__main__':
    s = solution()
    print(s.addNum(1))
    print(s.addNum(2))
    print(s.findMedian())
    print(s.addNum(3))
    print(s.findMedian())
