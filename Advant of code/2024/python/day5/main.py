"""
--- Day 5: Print Queue ---
Satisfied with their search on Ceres, the squadron of scholars suggests subsequently scanning the stationery stacks of sub-basement 17.

The North Pole printing department is busier than ever this close to Christmas, and while The Historians continue their search of this historically significant facility, an Elf operating a very familiar printer beckons you over.

The Elf must recognize you, because they waste no time explaining that the new sleigh launch safety manual updates won't print correctly. Failure to update the safety manuals would be dire indeed, so you offer your services.

Safety protocols clearly indicate that new pages for the safety manuals must be printed in a very specific order. The notation X|Y means that if both page number X and page number Y are to be produced as part of an update, page number X must be printed at some point before page number Y.

The Elf has for you both the page ordering rules and the pages to produce in each update (your puzzle input), but can't figure out whether each update has the pages in the right order.

"""
# ========================= PART 1 =========================

def printerQueue(rules,updates):
    rulesMap={}

    for x,y in rules:
        # x should be printed before y
        rulesMap[(x,y)]=True
        rulesMap[(y,x)]=False # y should not be printed before x

    def isValid(updates):
        n=len(updates)
        for i in range(n):
            for j in range(i+1,n):
                key=(updates[i],updates[j])
                if key in rulesMap and not rulesMap[key]:
                    return False
        return True
    ans=0

    for update in updates:
        if isValid(update):
            ans+=update[len(update)//2]

    return ans

# ========================= PART 2 =========================

def printQueueReorder(rules,updates):
    rulesMap={}

    for x,y in rules:
        # x should be printed before y
        rulesMap[(x,y)]=True
        rulesMap[(y,x)]=False # y should not be printed before x

    def isValid(updates):
        n=len(updates)
        for i in range(n):
            for j in range(i+1,n):
                key=(updates[i],updates[j])
                if key in rulesMap and not rulesMap[key]:
                    return False
        return True


    def reorder(updates):
        n=len(updates)
        for i in range(n):
            for j in range(i+1,n):
                key=(updates[i],updates[j])
                if key in rulesMap and not rulesMap[key]:
                    updates[i],updates[j]=updates[j],updates[i]
        return updates


    ans=0

    for update in updates:
        if not isValid(update):
            update=reorder(update)
            ans+=update[len(update)//2]

    return ans





import sys
if sys.argv[1]=="test":
    test_ip=open("./testcase.txt","r")
else:
    test_ip=open("./input.txt","r")

rules=[]


for line in test_ip:
    # if break comes in input then break the loop
    if line.isspace():
        break

    rules.append(list(map(int,line.split('|'))))

updates=[]
for line in test_ip:
    update=list(map(int,line.split(',')))
    updates.append(update)


print(printerQueue(rules,updates)) 
print(printQueueReorder(rules,updates))
