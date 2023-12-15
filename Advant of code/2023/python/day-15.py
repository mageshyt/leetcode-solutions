# --- Day 15: Lens Library ---


operations=open('../testcase.txt').read().split(',')
# print(lines)

def LensLibrary():
    pass


def part1():
    ans=0

    for instructions in operations:
        # print(">>",helper(total,op))
        ans+=hash(instructions)
    print("RESULT",ans)
    return ans


def hash(item):
    currVal=0
    print(">> ",item,currVal)
    for char in item:
        # convert from ascii to int
        res=ord(char)+currVal
        print(">> ",char,currVal,ord(char),res)
        res=res*17
        res=res%256
        print(res,char)

        # after all the operations then make currVal=res

        currVal=res
        print("==================")

    return currVal 



def part2():
    # (-) remove the label from the box
    # (=) add the label to the box

    boxes=[[] for _ in range(256)]
    focal_length={}
    print(boxes)

    for instructions in operations:
        if '-' in instructions:
            label=instructions[:-1]
            index=hash(label)
            if label in boxes[index]:
                boxes[index].remove(label)

        else:
            label,length=instructions.split('=')
            length=int(length)
            index=hash(label)

            if label not in boxes[index]:
                boxes[index].append(label)

            focal_length[label]=length

    print(focal_length)

    total=0
    for box_number, box in enumerate(boxes, 1):
        for lens_slot, label in enumerate(box, 1):
            total += box_number * lens_slot * focal_length[label]

    return total


print(part2())
# print(part1())