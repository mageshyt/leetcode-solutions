"""
There is a party where n friends numbered from 0 to n - 1 are attending. There is an infinite number of chairs in this party that are numbered from 0 to infinity. When a friend arrives at the party, they sit on the unoccupied chair with the smallest number.

For example, if chairs 0, 1, and 5 are occupied when a friend comes, they will sit on chair number 2.
When a friend leaves the party, their chair becomes unoccupied at the moment they leave. If another friend arrives at that same moment, they can sit in that chair.

You are given a 0-indexed 2D integer array times where times[i] = [arrivali, leavingi], indicating the arrival and leaving times of the ith friend respectively, and an integer targetFriend. All arrival times are distinct.

Return the chair number that the friend numbered targetFriend will sit on.


"""
from typing import List
import heapq
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:

        # add the friend number to the times list
        time=[(arrival, leaving, i) for i, (arrival, leaving) in enumerate(times)]

        # sort the time list by arrival time
        time.sort()

        # create a heap to store the chairs 
        used_chairs=[] #(leaving,chair)

        available_chairs=[i for i in range(len(time))]  # total no of chair needed

        for arrival, leaving, i in time:

            # if the friend is leaving, add the chair to available chairs 
            while used_chairs and used_chairs[0][0]<=arrival:
                _,chair=heapq.heappop(used_chairs)
                heapq.heappush(available_chairs,chair)

            chair=heapq.heappop(available_chairs)
            heapq.heappush(used_chairs,(leaving,chair)) 

            if i==targetFriend:
                return chair

        return -1

# time  complexity: O(nlogn) 

#Driver code
print(Solution().smallestChair([[1,4],[2,3],[4,6]],1)) #1

