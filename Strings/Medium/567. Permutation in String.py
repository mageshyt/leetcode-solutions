

import re


def checkInclusion(s1,s2):
    res=len(s1)
    for i in range(len(s2)):
        curr=s2[i]
        if curr in s1:
            nextPer=s2[i:i+len(s1)]
            print({nextPer})
            for char in s1:
                if char  in nextPer: res-=1
                else:break
            print(res,nextPer)
            if(res ==0): return True
        res=len(s1)


    print(res)
    return False 

s1 = "hello"
s2 ="ooolleoooleh"

print(checkInclusion(s1,s2))


