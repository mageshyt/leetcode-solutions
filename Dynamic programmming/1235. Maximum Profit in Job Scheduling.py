'''We have n jobs, where every job is scheduled to be done from startTime[i] to endTime[i], obtaining a profit of profit[i].

You're given the startTime, endTime and profit arrays, return the maximum profit you can take such that there are no two jobs in the subset with overlapping time range.

If you choose a job that ends at time X you will be able to start another job that starts at time X.

 

Example 1:



Input: startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]
Output: 120
Explanation: The subset chosen is the first and fourth job. 
Time range [1-3]+[3-6] , we get profit of 120 = 50 + 70.
Example 2:



Input: startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]
Output: 150
Explanation: The subset chosen is the first, fourth and fifth job. 
Profit obtained 150 = 20 + 70 + 60.
Example 3:



Input: startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]
Output: 6'''
import bisect

class Solution:
    def jobScheduling(self, s, e, p):
        jobs=sorted(zip(s,e,p))
        l=len(s) # number of jobs
        dp=[0]*len(jobs)

        for i in reversed(range(l)):
            end,profit=jobs[i][1],jobs[i][2]
            k=bisect_left(jobs,end,key=lambda j:j[0])  # type: ignore
            dp[i]=max(dp[i+1],profit+dp[k]) # previous max or current profit + max profit of previous jobs

        return dp[0]    

    
if __name__=='__main__':
    s=Solution()
    s.jobScheduling([1,2,3,3],[3,4,5,6],[50,10,40,70])
