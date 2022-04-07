def valid(s):
    dictval = {")": "(", "]": "[", "}": "{"} 
    stack = []
    for char in s:
        if char in dictval and len(stack) > 0:
            if stack.pop() != dictval[char]:  # if the popped value is not the corresponding opening parenthesis
                return False
        else:
            stack.append(char)

    return len(stack) == 0
print(valid('{[(]}'))