"""You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith event starts at startDayi and ends at endDayi, and if you attend this event, you will receive a value of valuei. You are also given an integer k which represents the maximum number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend the entire event. Note that the end day is inclusive: that is, you cannot attend two events where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events."""

import bisect
from typing import List
class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:

        # logic 
        # sort the events based on the end time
        # top down approach

        dp={}
        events.sort( )
        def helper(i,k):    
            if k==0 or i==len(events):
                return 0
            if (i,k) in dp:
                return dp[(i,k)]
            # now we can take the ith event or not take the ith event
            # Calculate the maximum value by considering the current event and skipping it

            start,end,value = events[i]

            # find the next event which starts after the current event ends
            j=bisect.bisect_left(events,[end+1])

            dp[(i,k)] = max(helper(i+1,k),helper(j,k-1)+value)


            return dp[(i, k)]

        return helper(0,k)
    
    # bottom up

 

    
if __name__ == "__main__":
    s=Solution()
    events = [[11,17,56],[24,40,53],[5,62,67],[66,69,84],[56,89,15]]
    k = 2
    print(s.maxValue(events,k))


        