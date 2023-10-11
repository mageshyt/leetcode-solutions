from typing import List
class Solution:
    # brute force
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        # lets sort the flowers by day

        flowers.sort(key=lambda x: x[0])

        # lets sort the people by their day
        people.sort()

        # lets create a result array
        result = [0] * len(people)


        for p, day in enumerate(people):

            # binary search using bisect

            left = 0
            right = len(flowers) - 1

            while left <= right:
                mid = (left + right) // 2

                if flowers[mid][0] <= day:
                    left = mid + 1
                else:
                    right = mid - 1

            # now we have the index of the flower that blooms after the person's day

            for i in range(0,left):
                # if the flower start and end is between the person's day

                if flowers[i][0] <= day and flowers[i][1] >= day:
                    result[p] += 1
        return result
    
    # using heap 
    def fullBloomFlowers(self,flowers,people):
        people=[(day,i) for i,day in enumerate(people)]
        res=[0] * len(people)

        import heapq

        start=[f[0] for f in flowers]
        end=[f[1] for f in flowers]

        # heapify the start and end
        heapq.heapify(start)
        heapq.heapify(end)

        # lets iterate over the people

        count=0

        for day,p in sorted(people):
            # lets pop all the flowers that have bloomed before the person's day
            while start and start[0] <= day:
                heapq.heappop(start)
                count+=1
            # lets pop all the flowers that have bloomed before the person's day
            while end and end[0] < day:
                heapq.heappop(end)
                count-=1
            # now we have the number of flowers that have bloomed before the person's day
            res[p] = count
            

        return res


if __name__ == "__main__":
    flowers = [[1,6],[3,7],[9,12],[4,13]]
    poeple = [2,3,7,11]

    print(Solution().fullBloomFlowers(flowers=flowers, people=poeple))