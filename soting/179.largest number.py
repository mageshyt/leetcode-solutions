
from typing import List
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        # convert to string
        nums=list(map(str,nums))
        # sort the list
        nums.sort(key=lambda x:x*10,reverse=True)

        return str(int(''.join(nums)))


if __name__ == '__main__':
    print("TESTING THE LARGEST NUMBER")
    s=Solution()
    print(s.largestNumber([10,2])) # 210
    print(s.largestNumber([3,30,34,5,9])) # 9534330
    print(s.largestNumber([1])) # 1
    print(s.largestNumber([0,0,0])) # 10
    print("END OF TESTIN")
        

        
