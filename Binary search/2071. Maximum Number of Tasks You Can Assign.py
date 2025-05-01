"""
You have n tasks and m workers. Each task has a strength requirement stored in a 0-indexed integer array tasks, with the ith task requiring tasks[i] strength to complete. The strength of each worker is stored in a 0-indexed integer array workers, with the jth worker having workers[j] strength. Each worker can only be assigned to a single task and must have a strength greater than or equal to the task's strength requirement (i.e., workers[j] >= tasks[i]).

Additionally, you have pills magical pills that will increase a worker's strength by strength. You can decide which workers receive the magical pills, however, you may only give each worker at most one magical pill.

Given the 0-indexed integer arrays tasks and workers and the integers pills and strength, return the maximum number of tasks that can be completed.

 

Example 1:

Input: tasks = [3,2,1], workers = [0,3,3], pills = 1, strength = 1
Output: 3
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 2 (0 + 1 >= 1)
- Assign worker 1 to task 1 (3 >= 2)
- Assign worker 2 to task 0 (3 >= 3)
Example 2:

Input: tasks = [5,4], workers = [0,0,0], pills = 1, strength = 5
Output: 1
Explanation:
We can assign the magical pill and tasks as follows:
- Give the magical pill to worker 0.
- Assign worker 0 to task 0 (0 + 5 >= 5)
Example 3:

Input: tasks = [10,15,30], workers = [0,10,10,10,10], pills = 3, strength = 10
Output: 2
Explanation:
We can assign the magical pills and tasks as follows:
- Give the magical pill to worker 0 and worker 1.
- Assign worker 0 to task 0 (0 + 10 >= 10)
- Assign worker 1 to task 1 (10 + 10 >= 15)
The last pill is not given because it will not make any worker strong enough for the last task.

"""
from typing import List
from collections import deque

class Solution:
    def maxTaskAssign(self, tasks: List[int], workers: List[int], pills: int, strength: int) -> int:
        """
        - u can assign pill only once to a worker
        - u can assign pill to any worker
        - only worker with strength >= task can do the task
        """
        # Sort the tasks and workers
        tasks.sort()
        workers.sort()

        left, right = 0, min(len(tasks), len(workers))
        def canAssign(mid):
            task_sub = tasks[:mid][::-1]
            avail = deque(workers[-mid:])
            used_pills = 0

            for task in task_sub:
                if avail and avail[-1] >= task:
                    avail.pop()  # Use strongest worker
                else:
                    worker_idx=bisect.bisect_left(avail,task-strength)
                    if worker_idx==len(avail) or used_pills==pills:
                        return False
                    used_pills+=1
                    avail.pop(worker_idx)
            return True
        while left < right:
            mid = (left + right + 1) // 2
            if canAssign(mid,):
                left = mid
            else:
                right = mid - 1

        return left


s=Solution()
print(s.maxTaskAssign([3,2,1], [0,3,3], 1, 1)) # Output: 3
