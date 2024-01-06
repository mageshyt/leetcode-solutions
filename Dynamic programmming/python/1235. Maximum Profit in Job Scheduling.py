
from bisect import bisect_left

class Solution:
    def jobScheduling(self, s, e, p):
        n=len(s)

        jobs=sorted(zip(s,e,p))   

        cache={}
        def dp(job):
            if job >= n:
                return 0
            
            if job in cache:
                return cache[job]
            
            taken=jobs[job][2] # take this job
            notTaken=dp(job+1)  # skip this job
            
           # find the next job with start time >= end time of current job
            
            nextJob=job+1

            while nextJob < n :
                start,end,_=jobs[nextJob]

                if start >= jobs[job][1]:
                    break

                nextJob+=1

            
            cache[job]=max(taken+dp(nextJob),notTaken )
            
            return cache[job]
        
        return dp(0)
    
    


s = [1,2,3,4,6]
e = [3,5,10,6,9]
p = [20,20,100,70,60]
print(Solution().jobScheduling(s,e,p))