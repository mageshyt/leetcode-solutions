
from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        # combine difficulty and profit into a list of tuples
        jobs = list(zip(difficulty, profit))
        # sort the jobs by difficulty
        jobs.sort()

        # sort the workers by ability
        worker.sort()

        # initialize the max profit and the current job index
        max_profit,i,best=0,0,0

        # iterate through the workers
        for ability in worker:
            # iterate through the jobs
            while i < len(jobs) and ability >= jobs[i][0]:
                # update the best profit
                best = max(best, jobs[i][1])
                i+=1

            # update the max profit
            max_profit += best

        return max_profit
    
# Time complexity: O(nlogn)
# Space complexity: O(n)

        