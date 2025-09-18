"""
There is a task management system that allows users to manage their tasks, each associated with a priority. The system should efficiently handle adding, modifying, executing, and removing tasks.

Implement the TaskManager class:

TaskManager(vector<vector<int>>& tasks) initializes the task manager with a list of user-task-priority triples. Each element in the input list is of the form [userId, taskId, priority], which adds a task to the specified user with the given priority.

void add(int userId, int taskId, int priority) adds a task with the specified taskId and priority to the user with userId. It is guaranteed that taskId does not exist in the system.

void edit(int taskId, int newPriority) updates the priority of the existing taskId to newPriority. It is guaranteed that taskId exists in the system.

void rmv(int taskId) removes the task identified by taskId from the system. It is guaranteed that taskId exists in the system.

int execTop() executes the task with the highest priority across all users. If there are multiple tasks with the same highest priority, execute the one with the highest taskId. After executing, the taskId is removed from the system. Return the userId associated with the executed task. If no tasks are available, return -1.

Note that a user may be assigned multiple tasks.
"""
import heapq
class TaskManager:

    """

    task - [userId, taskId, priority]
    guaranteed that task_id is unique when adding
    guaranteed that task_id exists when editing or removing

    """

    def __init__(self, tasks: List[List[int]]):
        self.task_map = {}
        self.heap = []
        for userId, taskId, priority in tasks:
            self.task_map[taskId] = (userId, priority)
            heapq.heappush(self.heap, (-priority, -taskId, userId))

    def add(self, userId: int, taskId: int, priority: int) -> None:
        self.task_map[taskId] = (userId, priority)
        heapq.heappush(self.heap, (-priority, -taskId, userId))
        

    def edit(self, taskId: int, newPriority: int) -> None:
        self.task_map[taskId] = (self.task_map[taskId][0], newPriority) # update priority
        userId = self.task_map[taskId][0]
        heapq.heappush(self.heap, (-newPriority, -taskId, userId))

    def rmv(self, taskId: int) -> None:
        if taskId in self.task_map:
            del self.task_map[taskId]

    def execTop(self) -> int:
        while self.heap:
            priority, taskId, userId = heapq.heappop(self.heap)
            taskId = -taskId
            priority = -priority
            if taskId in self.task_map and self.task_map[taskId][1] == priority and self.task_map[taskId][0] == userId:
                del self.task_map[taskId]
                return userId
        return -1

