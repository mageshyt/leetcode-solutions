

# ===================== PART 1 =====================
from typing import List
def isSave(report:List[int]):

    # Rules 
    """
    1 . report must be either increaing or decreasing
    2 . the diff between the two numbers atleast 1 and atmost 3 
    """


    if len(report) <=2:
        print(report)

    inc= report[1] > report[0]
    if inc:
        for i in range(1,len(report)):
            diff=report[i] - report[i-1]
            if not 1<=diff<=3:
                return False
        return True

    else:

        for i in range(1,len(report)):
            diff=report[i] - report[i-1]
            if not -3<=diff<=-1:
                return False
        
        return True

def saveReport1(reports: List[List[int]]):
    saveCount = 0

    for report in reports:
        if isSave(report):
            saveCount += 1
    return saveCount


# ===================== PART 2 =====================

def isReallySave(report:List[int]):
    if isSave(report):
        return True

    for i in range(len(report)):
        if isSave(report[:i]+report[i+1:]):
            return True

    return False

def saveReport2(reports: List[List[int]]):
    saveCount = 0

    for report in reports:
        if isReallySave(report):
            saveCount += 1


    return saveCount
# get the args if the args test then use tescase.txt file
# else use the input.txt file

import sys

if sys.argv[1]=="test":
    test_ip=open("./testcase.txt","r").read().split('\n')
else:
    test_ip=open("./input.txt","r").read().split('\n')


reports=[]
for i in test_ip:
    if i:
        reports.append([int(j) for j in i.split()])

print(saveReport1(reports))
print(saveReport2(reports))
