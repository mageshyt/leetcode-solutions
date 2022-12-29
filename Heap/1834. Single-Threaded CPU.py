'''You are given n​​​​​​ tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] means that the i​​​​​​th​​​​ task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks.

 

Example 1:

Input: tasks = [[1,2],[2,4],[3,2],[4,1]]
Output: [0,2,3,1]
Explanation: The events go as follows: 
- At time = 1, task 0 is available to process. Available tasks = {0}.
- Also at time = 1, the idle CPU starts processing task 0. Available tasks = {}.
- At time = 2, task 1 is available to process. Available tasks = {1}.
- At time = 3, task 2 is available to process. Available tasks = {1, 2}.
- Also at time = 3, the CPU finishes task 0 and starts processing task 2 as it is the shortest. Available tasks = {1}.
- At time = 4, task 3 is available to process. Available tasks = {1, 3}.
- At time = 5, the CPU finishes task 2 and starts processing task 3 as it is the shortest. Available tasks = {1}.
- At time = 6, the CPU finishes task 3 and starts processing task 1. Available tasks = {}.
- At time = 10, the CPU finishes task 1 and becomes idle.
'''
import heapq


class Solution:
    def getOrder(self, tasks):

        # add index to each task
        for i, task in enumerate(tasks):
            task.append(i)

        # sort by enqueue time
        tasks.sort(key=lambda x: x[0])

        # heap to store tasks sorted by processing time
        min_heap = []

        # time to keep track of current time
        time = tasks[0][0]

        # index to keep track of current task
        index = 0

        # result to store the order of tasks
        result = []

        # loop until all tasks are processed
        while min_heap or index < len(tasks):

            # if current time is greater >= task enqueue time
            while index < len(tasks) and time >= tasks[index][0]:
                # push task to heap [processing time, index]
                heapq.heappush(min_heap, [tasks[index][1], tasks[index][2]])
                print('pushing task to heap')
                index += 1

            # if heap is empty, we need to wait for next task to arrive
            if not min_heap:

                time = tasks[index][0]
            else:
                # pop task from heap
                processing_time, task_index = heapq.heappop(min_heap)
                # add task index to result
                result.append(task_index)
                # increment time
                time += processing_time

        return result


if __name__ == '__main__':
    tasks = [[1, 2], [2, 4], [3, 2], [4, 1]]
    print(Solution().getOrder(tasks))
