        for i in range(len(foods)):
                rating,cuisine,f=self.foodList[i]
                if rating>maxRating:
                    maxRating=rating
                    maxFood=f