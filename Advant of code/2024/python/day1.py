

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

    return sum((l_counter & r_counter).values())

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
