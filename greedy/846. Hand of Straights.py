
from typing import List
from collections import Counter,defaultdict
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if we can't divide the hand into groups of size groupSize, return False
        if len(hand)%groupSize!=0:
            return False

        # sort the hand
        hand.sort()

        # create a dictionary to store the count of each card
        cardCount= Counter(hand)

        # iterate through the hand and check if we can form groups of size groupSize
        for card in hand:
            if cardCount[card]>0:
                # loop through the next groupSize cards and decrement their count
                # if we can't form a group of size groupSize, return False
                for i in range(groupSize):
                    if card+i not in cardCount:
                        return False
                    cardCount[card+i]-=1
                    if cardCount[card+i]<0:
                        return False

        return True
