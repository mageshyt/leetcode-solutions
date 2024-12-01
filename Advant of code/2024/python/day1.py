

# ===================== PART 1 =====================
def findTotalDistance(left,right):
    # sort the left and right arrays
    left.sort()
    right.sort()

    # find the total distance
    total_distance=0
    print(left,right)
    for i in range(len(left)):

        total_distance+=abs(left[i]-right[i])

    return total_distance



# ===================== PART 2 =====================
from collections import Counter
def findSimilarity(left,right):
    l_counter=Counter(left)
    r_counter=Counter(right)

    total_similarity=0

    # print(l_counter,r_counter)

    for key,value in l_counter.items():
        if key in r_counter:
            total_similarity+=key*r_counter[key] * value

    return total_similarity




# get the args if the args test then use tescase.txt file
# else use the input.txt file

import sys

if sys.argv[1]=="test":
    test_ip=open("../testcase.txt","r").read().split()
else:
    test_ip=open("../input.txt","r").read().split()

nums=[int(i) for i in test_ip if i.isdigit()]
left=[]
right=[]
for i in range(len(nums)):
    if i%2==0:
        left.append(nums[i])
    else:
        right.append(nums[i])

print(findTotalDistance(left,right))
print(findSimilarity(left,right))
