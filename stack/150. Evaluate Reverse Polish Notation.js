`Evaluate the value of an arithmetic expression in Reverse Polish Notation.

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
Explanation: (4 + (13 / 5)) = 6`;

const evalRPN = (tokens) => {
  const stack = [];
  for (let i = 0; i < tokens.length; i++) {
    const curr = tokens[i];
    console.log(stack, curr);
    if (curr == "+") {
      stack.push(stack.pop() + stack.pop());
    } else if (curr == "-") {
      stack.push(-stack.pop() + stack.pop());
    } else if (curr == "*") {
      stack.push(stack.pop() * stack.pop());
    } else if (curr == "/") {
      const a = stack.pop();
      const b = stack.pop();
      stack.push(Math.trunc(b / a));
    } else {
      stack.push(parseInt(curr));
    }
  }
  return stack[0];
};

// console.log(evalRPN(["2", "1", "+", "3", "*"]));
console.log(evalRPN(["4", "13", "5", "/", "+"]));
