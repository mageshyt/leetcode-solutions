#second larges


def solution():
    nums=[3,2,4,5,1]
    largest=nums[0]
    second=nums[0]
    for num in nums:
        if  num > largest:
            second=largest
            largest=num
        elif num > second:
            second=num
    return second
print(solution())


def sol2():
    nums=[3,2,4,5,1]

    nums=list(set(nums))
    nums.sort()
    

sol2()