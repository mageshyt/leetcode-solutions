# --- Day 9: Mirage Maintenance ---

# Read input from file
with open('../testcase.txt') as fin:
    data = fin.read()
    lines = data.strip().split('\n')

# Convert each line to a list of integers
for idx, line in enumerate(lines):
    lines[idx] = [int(i) for i in line.split()]

print(len(lines))
def MirageMaintenance(input):
    # Uncomment the line below if you want to print the result of part 1
    print('>> Part 1  Answer :', part1())
    print('>> Part 2  Answer :', part2())

def findDifference(input):
    # Calculate the difference between consecutive elements in the input
    diff = []
    for idx, num in enumerate(input):
        if idx == 0:
            continue
        diff.append(num - input[idx - 1])
    return diff

def makeZero(input):
    # Iterate until all elements become zero
    steps = [input]
    while True:
        # If all the elements are zero, break the loop
        if all([num == 0 for num in input]):
            break

        # Reduce the input
        newInput = findDifference(input)
        

        # Add the steps
        steps.append(newInput)

        # Update the input
        input = newInput

    return steps

def part1():
    total = 0
    for idx, line in enumerate(lines):
        test = makeZero(line)

        for i in reversed(range(len(test) - 1)):
            prev = test[i + 1][-1]
            currentLast = test[i][-1]

            # Add the prev to the current
            test[i].append(prev + currentLast)

        # Add the end to the total
        total += test[0][-1]
    return total

def part2():
    total = 0
    res=[]
    for idx, line in enumerate(lines):
        test = makeZero(line)

        test[-1].insert(0, 0)

        for i in reversed(range(len(test) - 1)):
            prev = test[i + 1][0]
            currentLast = test[i][0]

            # Add the prev to the current
            test[i].insert(0, currentLast - prev)


        res.append(test[0][0])
        total += test[0][0]

    # print(len(res))
    # print(res)
    return total

# Call the MirageMaintenance function with the provided input
MirageMaintenance(lines)
