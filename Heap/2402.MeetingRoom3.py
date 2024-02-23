
from typing import List
import heapq
class Solution:
    def mostBooked(self,n:int,meetings:List[List[int]])->int:
        # sort the meeting by start time
        meetings.sort(key=lambda x:x[0] )
        print(meetings)

        available=[i for i in range(n) ]
        used=[] # (end_time,room_number)

        count=[0] * n # count[n]=meetings schedule

        for start,end in meetings:
            # Finish meetings


            while used and start >= used[0][0]:
                _,room=heapq.heappop(used)
                heapq.heappush(available,room)

            # no room is available

            if not available:
                end_time,room=heapq.heappop(used)
                end=end_time + (end - start ) # new end time for the current meeting
                heapq.heappush(available,room)


            # if room is available

            room=heapq.heappop(available) # get the room id
            heapq.heappush(used,(end,room))

            count[room]+=1

            


        return count.index(max(count)) # find first meeting room with max




if __name__ == "__main__":
    print(Solution().mostBooked(2,[[0,10],[4,5],[2,7]]))
