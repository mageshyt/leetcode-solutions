`implement a last-in-first-out (LIFO)
 stack using only two queues. 
 The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

void push(int x) Pushes element x to the top of the stack.
int pop() Removes the element on the top of the stack and returns it.
int top() Returns the element on the top of the stack.
boolean empty() Returns true if the stack is empty, false otherwise.
Notes:

You must use only standard operations of a queue, which means that only push to back, peek/pop from front, size and is empty operations are valid.
Depending on your language, the queue may not be supported natively. You may simulate a queue using a list or deque (double-ended queue) as long as you use only a queue's standard operations.
 

Example 1:

Input
["MyStack", "push", "push", "top", "pop", "empty"]
[[], [1], [2], [], [], []]
Output
[null, null, null, 2, 2, false]

Explanation
MyStack myStack = new MyStack();
myStack.push(1);
myStack.push(2);
myStack.top(); // return 2
myStack.pop(); // return 2
myStack.empty(); // return False


 `;

class MyStack {
  constructor() {
    this.queue1 = [];
    this.queue2 = [];
  }
  push(x) {
    this.queue1.push(x);
  }
  pop() {
    while (this.queue1.length > 1) {
      this.queue2.push(this.queue1.shift());
    }
    const res = this.queue1.shift();
    `
    what we are doing here means 
    ex:
    q1=[1,2,3,4]
    after fist shift, q2=[1,2,3] , q1=[4] so remove 4 from q1 so it will pop element 4
    in second loop 
    q1=[1,2,3] q2=[]
    `;
    while (this.queue2.length > 0) {
      this.queue1.push(this.queue2.shift());
    }
    return res;
  }
  top() {
    const res = this.queue1[this.queue1.length - 1];

    return res;
  }
  empty() {
    return this.queue1.length === 0;
  }
}
const stack = new MyStack();
stack.push(1);
stack.push(2);
stack.push(3);
stack.push(4);
console.log(stack.top());
console.log(stack.pop());
