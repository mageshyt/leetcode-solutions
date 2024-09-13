from typing import List
class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        res=[]

        for q in queries:
            xor=0

            for i in range(q[0],q[1]+1):
                xor^=arr[i]

            res.append(xor)





        return res

if __name__ == '__main__':
    arr = [1,3,4,8]
    queries = [[0,1],[1,2],[0,3],[3,3]]

    s=Solution()
    res=s.xorQueries(arr,queries)
    print(res)

