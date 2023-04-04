"""We are given an array asteroids of integers representing asteroids in a row.

For each asteroid, the absolute value represents its size, and the sign represents its direction (positive meaning right, negative meaning left). Each asteroid moves at the same speed.

Find out the state of the asteroids after all collisions. If two asteroids meet, the smaller one will explode. If both are the same size, both will explode. Two asteroids moving in the same direction will never meet.

 

Example 1:

Input: asteroids = [5,10,-5]
Output: [5,10]
Explanation: The 10 and -5 collide resulting in 10. The 5 and 10 never collide.
Example 2:

Input: asteroids = [8,-8]
Output: []
Explanation: The 8 and -8 collide exploding each other.
Example 3:

Input: asteroids = [10,2,-5]
Output: [10]
Explanation: The 2 and -5 collide resulting in -5. The 10 and -5 collide resulting in 10.
 """


class Solution:
    def asteroidCollision(self, asteroids):

        stack = []
        for rocks in asteroids:
            # if in same direction
            if rocks > 0:
                stack.append(rocks)

            else:
                while stack and stack[-1] > 0 and stack[-1] < abs(rocks):
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(rocks)
                elif stack[-1] == abs(rocks):
                    stack.pop()

        return stack


if __name__ == "__main__":
    print(Solution().asteroidCollision([5, 10, -5]))
    print(Solution().asteroidCollision([8, -8]))
    print(Solution().asteroidCollision([10, 2, -5]))
