class Solution:
    def findComplement(self, num: int) -> int:

        temp= num

        i=0

        while temp>0:
            temp= temp>>1
            i+=1

        mask= (1<<i)-1

        return num^mask

# Time complexity: O(1)
# Space complexity: O(1)
