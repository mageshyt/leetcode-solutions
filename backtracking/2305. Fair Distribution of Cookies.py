class Solution:
    def distributeCookies(self,cookies,k):
        min_unfairness = float('inf')

        children_distribution= [0] * k


        def backTrack(i):
            # base case
            nonlocal min_unfairness,children_distribution
            if i == len(cookies):
                min_unfairness=min(min_unfairness,max(children_distribution))
                return
            
            if min_unfairness <= max(children_distribution):
                return
            
            

            # recursive case
            for j in range(k):
                children_distribution[j]+=cookies[i]
                backTrack(i+1)
                children_distribution[j]-=cookies[i]

        backTrack(0)

        return min_unfairness
    


print(Solution().distributeCookies([1,2,3,4,5],3))
            
