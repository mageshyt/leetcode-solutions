
"""
    --- Day 3: Mull It Over ---
"Our computers are having issues, so I have no idea if we have any Chief Historians in stock! You're welcome to check the warehouse, though," says the mildly flustered shopkeeper at the North Pole Toboggan Rental Shop. The Historians head out to take a look.

The shopkeeper turns to you. "Any chance you can see why our computers are having issues again?"

The computer appears to be trying to run a program, but its memory (your puzzle input) is corrupted. All of the instructions have been jumbled up!

It seems like the goal of the program is just to multiply some numbers. It does that with instructions like mul(X,Y), where X and Y are each 1-3 digit numbers. For instance, mul(44,46) multiplies 44 by 46 to get a result of 2024. Similarly, mul(123,4) would multiply 123 by 4.

However, because the program's memory has been corrupted, there are also many invalid characters that should be ignored, even if they look like part of a mul instruction. Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

For example, consider the following section of corrupted memory:

xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))
Only the four highlighted sections are real mul instructions. Adding up the result of each instruction produces 161 (2*4 + 5*5 + 11*8 + 8*5).

Scan the corrupted memory for uncorrupted mul instructions. What do you get if you add up all of the results of the multiplications?
    
"""
# ========================= PART 1 =========================
import re
def curreptedMul(instruction:str):
    regx=re.findall(f"mul\((\d+),(\d+)\)",instruction)

    result=0

    for paris in regx:
        result+=int(paris[0])*int(paris[1])

    return result

# ========================= PART 2 =========================

def curruptedMul2(instruction:str):
    regx=re.findall(f"mul\(\d+,\d+\)|do\(\)|don't\(\)",instruction)
    result=0
    isMul=True

    for operation in regx:
        # print(operation)
        if "mul" in operation and  isMul:
            nums=re.findall("\d+",operation)
            # print(nums)
            result+=int(nums[0])*int(nums[1])
        elif "do()" == operation:
            isMul=True
        elif "don't()" == operation:
            isMul=False
        # print("-----------------")


    return result



import sys

if sys.argv[1]=="test":
    test_ip=open("./testcase.txt","r").read()
else:
    test_ip=open("./input.txt","r").read()


print(curreptedMul(test_ip))
print(curruptedMul2(test_ip))
