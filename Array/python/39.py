class Solution:
    def combinationSum(self, candidates, target: int) :
        candidates.sort()
        res=[]
        def helper(target,path,candidates,result):
            if target == 0: 
                result.append(path)
            
            for i in range(len(candidates)):
                if target < candidates[i]: return
                new_target=target - candidates[i]
                
                newpath=[]
                newpath.extend(path)
                newpath.append(candidates[i])
                print(new_target,newpath)
                
                helper(new_target,newpath,candidates[0:i],result)
                
        helper(target,[],candidates,res)
        print(res)
        return res
                

s=Solution()
s.combinationSum([2,3,6,7],7)