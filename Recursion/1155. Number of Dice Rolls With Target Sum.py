class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        cache={}
        def dfs(n,k,target):

            if (n,k,target) in cache:
                return cache[(n,k,target)]
            
            if n==0 and target==0:
                return 1
            
            if n==0 or target==0:
                return 0
            
            ans=0
            for i in range(1,k+1):
                if target-i>=0:
                    ans+=dfs(n-1,k,target-i)

            cache[(n,k,target)]=ans

            return ans
        
        return dfs(n,k,target)%(10**9+7)
    

if __name__ == "__main__":
    print(Solution().numRollsToTarget(30,30,500))