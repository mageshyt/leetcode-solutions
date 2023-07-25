
import heapq


class SmallestInfiniteSet:

    def __init__(self):
        self.minHeap = []
        self.hashMap = {}
        self.currentNum = 1

    def popSmallest(self) -> int:
        temp = self.currentNum

        if (self.minHeap):
            pop = heapq.heappop(self.minHeap)
            self.hashMap.pop(pop)

            return pop
        else:
            self.currentNum += 1
            return temp

    def addBack(self, num: int) -> None:
        if (num < self.currentNum and num not in self.hashMap):
            heapq.heappush(self.minHeap, num)
            self.hashMap[num] = True


if __name__ == '__main__':
    obj = SmallestInfiniteSet()
    print(
        obj.popSmallest(),
        obj.addBack(5),
        obj.addBack(7),
        obj.popSmallest(),
        obj.addBack(1),
        obj.minHeap,
        obj.popSmallest(),
    )
