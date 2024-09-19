from typing import List
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        
        operators={
                '+':lambda x,y:x+y,
                '-':lambda x,y:x-y,
                '*':lambda x,y:x*y
                }

        def backtack(left,right):
            res=[]

            for i in range(left,right+1):
                op=expression[i]
                # check if the operator is in the operators
                if op in operators:
                    leftRes=backtack(left,i-1)
                    rightRes=backtack(i+1,right)

                    for l in leftRes:
                        for r in rightRes:
                            res.append(operators[op](l,r))

            if not res:

                res.append(int(expression[left:right+1]))

            return res

        return backtack(0,len(expression)-1)

if __name__ == '__main__':
    print("TESTING THE DIFFERENT WAYS TO COMPUTE")
    s=Solution()
    print(s.diffWaysToCompute("2-1-1")) # [0,2]
    print(s.diffWaysToCompute("2*3-4*5")) # [-34,-14,-10,-10,10]
    print("END OF TESTING")
