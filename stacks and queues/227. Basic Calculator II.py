class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        # remove space
        s = s.replace(" ", "")

        stack = []

        op = '+'  # current operator
        curr = 0  # current number

        for char in s:
            if char.isdigit():
                curr = curr*10 + int(char)

            if char in '+-*/' or char == s[-1]:
                if op == '+':
                    stack.append(curr)
                elif op == '-':
                    stack.append(-curr)
                elif op == '*':
                    stack.append(stack.pop()*curr)
                elif op == '/':
                    stack.append(int(stack.pop()/curr))
                op = char
                curr = 0

        return sum(stack)



if __name__ == "__main__":

    print(Solution().calculate("3+2*2"))
