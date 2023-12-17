from typing import List
import heapq
from collections import defaultdict
from sortedcontainers import SortedSet
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    
        self.cuisineMap=defaultdict(SortedSet) # cuisine: [rating ,food]
        self.hashMap=defaultdict(tuple) # food: (rating,cuisine,food)

        for i in range(len(foods)):
            self.cuisineMap[cuisines[i]].add((-ratings[i],foods[i]))
            self.hashMap[foods[i]]=(cuisines[i],ratings[i])


        # heapq.heapify(self.foodList)

    def changeRating(self, food: str, newRating: int) -> None:
        
        c,r=self.hashMap[food]
        self.cuisineMap[c].remove((-r,food))
        self.cuisineMap[c].add((-newRating,food))

        self.hashMap[food]=(c,newRating)
    def highestRated(self, cuisine: str) -> str:
        return self.cuisineMap[cuisine][0][1]


        # return heapq.heappop(self.foodList



   
    




# Your FoodRatings object will be instantiated and called as such:
foods=["P","B","Burger","Salad","AM"]
cuisines=["Italian","Italian","American","Health","Italian"]
ratings=[4,3,2,5,6]
obj = FoodRatings(foods, cuisines, ratings)

obj.changeRating("P",6)

param_2 = obj.highestRated("Italian")

print(param_2)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)