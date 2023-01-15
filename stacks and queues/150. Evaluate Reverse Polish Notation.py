'''Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22'''


class Solution:
    def evalRPN(self, tokens) :
        stack=[]
        for i in tokens:
            if i not in "-+/*":
                stack.append(int(i))
            else:
                a=stack.pop()
                b=stack.pop()
                if i=='+':
                    stack.append(b+a)
                elif i=='-':
                    stack.append(b-a)
                elif i=='*':
                    stack.append(b*a)
                elif i=='/':
                    stack.append(int(b/a))

        return stack.pop()


if __name__=='__main__':
    tokens=["2","1","+","3","*"]
    s=Solution()
    print(s.evalRPN(tokens))


