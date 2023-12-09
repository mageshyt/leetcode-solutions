# --- Day 8: Haunted Wasteland ---

from collections import defaultdict
from typing import List
import math

with open("../testcase.txt") as fin:
    data = fin.read()
    lines = data.strip().split("\n")
# print(lines)
class Solution:
    def __init__(self):
        self.instruction=lines[0]
        nodes = lines[2:]

        self.nodes = {}

        for node in nodes:
            node = node.split(" ")

            navigation = (node[2]+node[3]).replace("(","").replace(")","").split(",")

            # print(navigation)

            self.nodes[node[0]] = {
                "L": navigation[0],
                "R": navigation[1],
            }

        
    def HauntedWasteland(self, input):

        print(">> Part 1  Answer :",self.part1())
        
        print(">> Part 2  Answer :",self.part2())
        

    def part1(self):
        cost=0

        start="AAA"
        end="ZZZ"

       

        while start != end:

            for nav in self.instruction:
                if nav == "L":
                    start = self.nodes[start]["L"]
                    cost+=1
                elif nav == "R":
                    start = self.nodes[start]["R"]
                    cost+=1
                else:
                    print("Error")
                    break

        return cost




    def part2(self):
        cost=0

        starts=[ n for n in self.nodes if n[2] =='A']

        

        ends=[ n for n in self.nodes if n[2] =='Z']

        print(starts,ends)

        cur=[self.helper(start,ends) for start in starts]

        print(cur)

        return math.lcm(*cur)
    

    def helper(self, start,ends):

        cost=0

        while start not in ends :
            for nav in self.instruction:
                if nav == "L":
                    start = self.nodes[start]["L"]
                    cost+=1
                elif nav == "R":
                    start = self.nodes[start]["R"]
                    cost+=1
                else:
                    print("Error")
                    break

        return cost





if __name__ == "__main__":
    s = Solution()
    s.HauntedWasteland(lines)
    # print(s.part1(lines))
    # print(s.part2(lines))