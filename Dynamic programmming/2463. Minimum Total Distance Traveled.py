"""
There are some robots and factories on the X-axis. You are given an integer array robot where robot[i] is the position of the ith robot. You are also given a 2D integer array factory where factory[j] = [positionj, limitj] indicates that positionj is the position of the jth factory and that the jth factory can repair at most limitj robots.

The positions of each robot are unique. The positions of each factory are also unique. Note that a robot can be in the same position as a factory initially.

All the robots are initially broken; they keep moving in one direction. The direction could be the negative or the positive direction of the X-axis. When a robot reaches a factory that did not reach its limit, the factory repairs the robot, and it stops moving.

At any moment, you can set the initial direction of moving for some robot. Your target is to minimize the total distance traveled by all the robots.

Return the minimum total distance traveled by all the robots. The test cases are generated such that all the robots can be repaired.

Note that

All robots move at the same speed.
If two robots move in the same direction, they will never collide.
If two robots move in opposite directions and they meet at some point, they do not collide. They cross each other.
If a robot passes by a factory that reached its limits, it crosses it as if it does not exist.
If the robot moved from a position x to a position y, the distance it moved is |y - x|.
 

Example 1:


Input: robot = [0,4,6], factory = [[2,2],[6,2]]
Output: 4
Explanation: As shown in the figure:
- The first robot at position 0 moves in the positive direction. It will be repaired at the first factory.
- The second robot at position 4 moves in the negative direction. It will be repaired at the first factory.
- The third robot at position 6 will be repaired at the second factory. It does not need to move.
The limit of the first factory is 2, and it fixed 2 robots.
The limit of the second factory is 2, and it fixed 1 robot.
The total distance is |2 - 0| + |2 - 4| + |6 - 6| = 4. It can be shown that we cannot achieve a better total distance than 4.
Example 2:


Input: robot = [1,-1], factory = [[-2,1],[2,1]]
Output: 2
Explanation: As shown in the figure:
- The first robot at position 1 moves in the positive direction. It will be repaired at the second factory.
- The second robot at position -1 moves in the negative direction. It will be repaired at the first factory.
The limit of the first factory is 1, and it fixed 1 robot.
The limit of the second factory is 1, and it fixed 1 robot.
The total distance is |2 - 1| + |(-2) - (-1)| = 2. It can be shown that we cannot achieve a better total distance than 2.
 

Constraints:
"""

from typing import List
class Solution:
    def minimumTotalDistance(self, robot: List[int], factory: List[List[int]]) -> int:
        # sort the robot and factory by their position
        robot.sort()
        factory.sort()

        factoreis=[]
        for factory_pos,limit in factory:
            for _ in range(limit):
                factoreis.append(factory_pos)


        # print(factoreis)
        dp={}

        def dfs(robo_pos,factor_pos):
            if robo_pos<0:
                return 0
            # if some robot are not fixed but no factory left
            if factor_pos<0:
                return float('inf')
            if (robo_pos,factor_pos) in dp:
                return dp[(robo_pos,factor_pos)]

            # choice 1 : repaire
            distance=abs(robot[robo_pos]-factoreis[factor_pos])
            repair= dfs(robo_pos-1,factor_pos-1)+distance

            # choice 2: not repaire
            not_repair=dfs(robo_pos,factor_pos-1)

            dp[(robo_pos,factor_pos)]=min(repair,not_repair)
            return dp[(robo_pos,factor_pos)]

        return dfs(len(robot)-1,len(factoreis)-1)

robot = [0,4,6]
factory = [[2,2],[6,2]]
print(Solution().minimumTotalDistance(robot,factory))
