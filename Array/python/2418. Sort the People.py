from typing import List
class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        people=zip(names,heights )
        # sort the people based on the height and then the name
        people=sorted(people,key=lambda x: (-x[1],x[0]))

        return [name for name,_ in people]

print(Solution().sortPeople(["Alex","Ben","Charlie","David"],[5,3,2,6])) # ["David","Alex","Ben","Charlie"]
