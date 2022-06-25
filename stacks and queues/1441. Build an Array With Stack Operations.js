`ou are given an array target and an integer n.

In each iteration, you will read a number from list = [1, 2, 3, ..., n].

Build the target array using the following operations:

"Push": Reads a new element from the beginning list, and pushes it in the array.
"Pop": Deletes the last element of the array.
If the target array is already built, stop reading more elements.
Return a list of the operations needed to build target. The test cases are generated so that the answer is unique.

 

Example 1:

Input: target = [1,3], n = 3
Output: ["Push","Push","Pop","Push"]
Explanation: 
Read number 1 and automatically push in the array -> [1]
Read number 2 and automatically push in the array then Pop it -> [1]
Read number 3 and automatically push in the array -> [1,3]
Example 2:

Input: target = [1,2,3], n = 3
Output: ["Push","Push","Push"]
Example 3:

Input: target = [1,2], n = 4
Output: ["Push","Push"]
Explanation: You only need to read the first 2 numbers and stop.`;

const buildArray = (target, n) => {
  const stack = [];
  let count = 0;

  for (let i = 1; i <= n; i++) {
    if (count === target.length) break;
    if (target.includes(i)) {
      stack.push("Push");
      count++;
    } else {
      stack.push("push");
      stack.push("Pop");
    }
  }
  return stack;
};

console.log(buildArray([1, 3], 3));

console.log(buildArray([1, 2], 4));
