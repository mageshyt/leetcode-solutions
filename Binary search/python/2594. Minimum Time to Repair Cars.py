
import math
class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        """
        - we can repair all car simultaneously
        - rank r can repair r * n^2
        - find min time take 
        """

        max_cars=cars//len(ranks)+1
        low,high=1,min(ranks) * cars * max_cars

        def can_we_repair(time):
            cnt=0
            for rank in ranks:
                # n formula  is  (time)/(r) *  ^ (1/2)
                no_of_cars=math.sqrt(time//rank)
                cnt+=int(no_of_cars)

            return cnt >= cars

        while low <= high:

            mid=low+(high-low)//2
            if can_we_repair(mid):
                # if we can place in x min we can place in x+1 min also so reduce space to find the better time
                high=mid-1
            else:
                low=mid+1

        return low 

