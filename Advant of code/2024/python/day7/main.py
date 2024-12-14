"""
--- Day 7: Bridge Repair ---
The Historians take you to a familiar rope bridge over a river in the middle of a jungle. The Chief isn't on this side of the bridge, though; maybe he's on the other side?

When you go to cross the bridge, you notice a group of engineers trying to repair it. (Apparently, it breaks pretty frequently.) You won't be able to cross until it's fixed.

You ask how long it'll take; the engineers tell you that it only needs final calibrations, but some young elephants were playing nearby and stole all the operators from their calibration equations! They could finish the calibrations if only someone could determine which test values could possibly be produced by placing any combination of operators into their calibration equations (your puzzle input).
"""
from collections import defaultdict
# ========================= PART 1 =========================
def brideBreaker1(stoleOperator):
    res=defaultdict(int)

    def backtrack(curr,idx,target,arr):
        if idx==len(arr):
            if curr==target:
                key="-".join(map(str,arr))
                res[key]=curr
            return

        if curr>target:
            return

        backtrack(curr+arr[idx],idx+1,target,arr)
        backtrack(curr*arr[idx],idx+1,target,arr)



    for target,values in stoleOperator:
        # print(target,values)
        backtrack(0,0,target,values)

    return sum(res.values())

# ========================= PART 2 =========================
def brideBreaker2(stoleOperator):
    res=defaultdict(int)

    def backtrack(curr,idx,target,arr):
        if idx==len(arr):
            if curr==target:
                key="-".join(map(str,arr))
                res[key]=curr
            return

        if curr>target:
            return

        backtrack(curr+arr[idx],idx+1,target,arr)
        backtrack(curr*arr[idx],idx+1,target,arr)
        concat=int(str(curr)+str(arr[idx]))
        backtrack(concat,idx+1,target,arr)



    for target,values in stoleOperator:
        # print(target,values)
        backtrack(0,0,target,values)

    return sum(res.values())






import sys
if sys.argv[1]=="test":
    test_ip=open("./testcase.txt","r").read().strip().split("\n")
else:
    test_ip=open("./input.txt","r").read().strip().split("\n")


stoleOperator=[]

for rope in test_ip:
    target,values=rope.split(":")
    values=list(map(int,values.strip().split(" ")))

    stoleOperator.append((int(target),values))

print(brideBreaker1(stoleOperator))
print(brideBreaker2(stoleOperator))

