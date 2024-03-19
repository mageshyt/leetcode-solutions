'''Given a characters array tasks, representing the tasks a CPU needs to do, where each letter represents a different task. Tasks could be done in any order. Each task is done in one unit of time. For each unit of time, the CPU could complete either one task or just be idle.

However, there is a non-negative integer n that represents the cooldown period between two same tasks (the same letter in the array), that is that there must be at least n units of time between any two same tasks.

Return the least number of units of times that the CPU will take to finish all the given tasks.

 

Example 1:

Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: 
A -> B -> idle -> A -> B -> idle -> A -> B
There is at least 2 units of time between any two same tasks.
Example 2:

Input: tasks = ["A","A","A","B","B","B"], n = 0
Output: 6
Explanation: On this case any permutation of size 6 would work since n = 0.
["A","A","A","B","B","B"]
["A","B","A","B","A","B"]
["B","B","B","A","A","A"]
...
And so on.
Example 3:

Input: tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2
Output: 16
Explanation: 
One possible solution is
A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> idle -> idle -> A -> idle -> idle -> A'''

from collections import Counter, deque
import heapq


class Solution:
    def leastInterval(self, tasks, n: int) -> int:
        hash_map = Counter(tasks)

        # we are going to use max heap to store the tasks and queue to store the tasks need to do
        max_heap = [-val for val in hash_map.values()]
        heapq.heapify(max_heap)

        queue = deque()

        time_taken = 0

        while max_heap or queue:

            time_taken += 1

            if max_heap:
                # we are adding 1 to the task count to make it positive
                next_task = heapq.heappop(max_heap) + 1
                time_for_next_task = time_taken + n  # available time for next task
                # add to queue if there is still work to do
                if next_task:  # if next_task is 0, then there is no work to do
                    queue.append([next_task, time_for_next_task])

            # if queue is not empty and the time for next task is available
            if queue and queue[0][1] == time_taken:
                pop = queue.popleft()[0]  # get the task count
                heapq.heappush(max_heap, pop)  # add to max heap

        return time_taken

    def leastInterval(self, tasks, n: int) -> int:
        # count the occurences of each task
        hash_map = Counter(tasks)

        max_heap=[-val for val in hash_map.values()] # we are going to use max heap to store the tasks
        heapq.heapify(max_heap)

        time_taken = 0

        queue=deque()

        while max_heap or queue:
            # increase the time
            time_taken+=1

            if max_heap:
                # we are adding 1 to the task count to make it positive
                next_task=heapq.heappop(max_heap)+1
                time_for_next_task=time_taken+n

                # push to queue if there is still work to do
                if next_task:
                    queue.append([next_task, time_for_next_task])

            # if queue is not empty and the time for next task is available
            if queue and queue[0][1]==time_taken:
                pop=queue.popleft()[0]
                heapq.heappush(max_heap, pop)
    
        return time_taken


if __name__ == '__main__':
    s = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    n = 2
    print(s.leastInterval(tasks, n))
