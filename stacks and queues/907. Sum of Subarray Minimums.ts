`Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
`;

const sumSubarrayMins = (arr: number[]) => {
  let left_to_right: number[] = new Array(arr.length).fill(0);

  let stack: number[] = [];

  for (let i = 0; i < arr.length; i++) {
    while (stack.length && arr[stack[stack.length - 1]] > arr[i]) {
      // if the current element is smaller than the top of the stack, pop the stack
      left_to_right[stack.pop()!] = i;
    }
    stack.push(arr[i]);
  }

  // now right ot left
  let right_to_left: number[] = new Array(arr.length).fill(-1);
  stack = []; // reset the stack
  // going from right to left to find the left boundry
  for (let i = arr.length - 1; i >= 0; i--) {
    while (stack.length && arr[stack[stack.length - 1]] >= arr[i]) {
      // if the current element is smaller than the top of the stack, pop the stack
      right_to_left[stack.pop()!] = i;
    }
    stack.push(arr[i]);
  }

  let res = 0;
  for (let i = 0; i < arr.length; i++) {
    let [left, right] = [right_to_left[i], left_to_right[i]];
    res += (right - i) * (i - left) * arr[i];
    res %= 1000000007;
  }
  return res;
};

console.log(sumSubarrayMins([3, 1, 2, 4]));
