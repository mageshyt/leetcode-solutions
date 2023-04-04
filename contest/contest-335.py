"""2583. Kth Largest Sum in a Binary Tree"""

"""You are given the root of a binary tree and a positive integer k.

The level sum in the tree is the sum of the values of the nodes that are on the same level.

Return the kth largest level sum in the tree (not necessarily distinct). If there are fewer than k levels in the tree, return -1.

Note that two nodes are on the same level if they have the same distance from the root."""




from collections import *
import heapq
class Solution:
    def kthLargestLevelSum(self, root, k: int) -> int:
        if not root:
            return -1

        queue = deque()

        queue.append(root)

        level_sum = []

        while queue:

            # add val in node
            heapq.heappush(level_sum, sum([node.val for node in queue]))

            for _ in range(len(queue)):
                popped = queue.popleft()
                if popped.left:
                    queue.append(popped.left)
                if popped.right:
                    queue.append(popped.right)

        if len(level_sum) < k:
            return -1

        return heapq.nlargest(k, level_sum)[-1]


"""2582. Pass the Pillow"""


"""There are n people standing in a line labeled from 1 to n. The first person in the line is holding a pillow initially. Every second, the person holding the pillow passes it to the next person standing in the line. Once the pillow reaches the end of the line, the direction changes, and people continue passing the pillow in the opposite direction.

For example, once the pillow reaches the nth person they pass it to the n - 1th person, then to the n - 2th person and so on.
Given the two positive integers n and time, return the index of the person holding the pillow after time seconds.

   

Example 1:

Input: n = 4, time = 5
Output: 2
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3 -> 4 -> 3 -> 2.
Afer five seconds, the pillow is given to the 2nd person.
Example 2:

# Input: n = 3, time = 2
Output: 3
Explanation: People pass the pillow in the following way: 1 -> 2 -> 3.
Afer two seconds, the pillow is given to the 3rd person."""


def passThePillow(n: int, time: int) -> int:
    round = time // (n-1)
    print(round)
    res = 0
    if round % 2 == 0:
        res = (time % (n-1)) + 1
    else:
        res = n - time % (n-1)

    return res


print(passThePillow(6, 100))
