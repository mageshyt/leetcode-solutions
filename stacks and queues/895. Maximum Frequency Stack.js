`Design a stack-like data structure to push elements to the stack and pop the most frequent element from the stack.

Implement the FreqStack class:

FreqStack() constructs an empty frequency stack.
void push(int val) pushes an integer val onto the top of the stack.
int pop() removes and returns the most frequent element in the stack.
If there is a tie for the most frequent element, the element closest to the stack's top is removed and returned.
 

Example 1:

Input
["FreqStack", "push", "push", "push", "push", "push", "push", "pop", "pop", "pop", "pop"]
[[], [5], [7], [5], [7], [4], [5], [], [], [], []]
Output
[null, null, null, null, null, null, null, 5, 7, 5, 4]

Explanation
FreqStack freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop();   // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop();   // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop();   // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].`;

class FreqStack {
  constructor() {
    this.stackMap = new Map();
    this.map = new Map();
    this.maxFreq = 0;
  }
  push(val) {
    const newFreq = this.map.get(val) + 1 || 1;
    this.maxFreq = Math.max(this.maxFreq, newFreq);
    this.map.set(val, newFreq);

    // ! operation in stackMap
    const frequent_val_stack = this.stackMap.has(newFreq)
      ? this.stackMap.get(newFreq)
      : [];
    frequent_val_stack.push(val);
    `
    Key -->  number of time element present in the array
    values --> [the elements present in the array at that particular frequency]] 
    Example:
        array=[5,6,2,7,2,5,2]
        here our map will be like 
        stackMap: 1-->[5,6,7,2] , 2-->[5,2], 3-->[2]
    `;

    //! update stackMap
    this.stackMap.set(newFreq, frequent_val_stack);
  }
  pop() {
    let frequent_val = this.stackMap.get(this.maxFreq);
    const Top_val = frequent_val.pop();
    this.map.set(Top_val, this.maxFreq - 1); // ! update the map
    // console.log({ max: this.maxFreq, frequent_val, Top_val, map: this.map });

    `
    example:
    array=[5,6,2,7,2,5,2]
    here our map will be like
    stackMap: 1-->[5,6,7,2] , 2-->[5,2], 3-->[2]
    maxFreq=3
    frequent_val= [5] if we pop 5 
    Top_val=5

    we will update the map
     Map(3) { 5 => 2, 7 => 2, 4 => 1 }

    `;

    // ! if our freq val array is empty then remove it from stackMap and decrement maxFreq by 1
    if (frequent_val.length === 0) {
      this.stackMap.delete(this.maxFreq);

      this.maxFreq--;
    }
    return Top_val;
  }
}
const freqStack = new FreqStack();
freqStack.push(5); // The stack is [5]
freqStack.push(7); // The stack is [5,7]
freqStack.push(5); // The stack is [5,7,5]
freqStack.push(7); // The stack is [5,7,5,7]
freqStack.push(4); // The stack is [5,7,5,7,4]
freqStack.push(5); // The stack is [5,7,5,7,4,5]
freqStack.pop(); // return 5, as 5 is the most frequent. The stack becomes [5,7,5,7,4].
freqStack.pop(); // return 7, as 5 and 7 is the most frequent, but 7 is closest to the top. The stack becomes [5,7,5,4].
freqStack.pop(); // return 5, as 5 is the most frequent. The stack becomes [5,7,4].
freqStack.pop(); // return 4, as 4, 5 and 7 is the most frequent, but 4 is closest to the top. The stack becomes [5,7].`;
