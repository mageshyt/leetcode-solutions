`You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

 

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
Example 2:

Input: nums = [1], k = 1
Output: [1]`;


const maxSlidingWindow = (nums, k) => {
  const output = [];
  const deque = [];

  let right = 0;

  while (right < nums.length) {
    // remove the smaller value from the deque
    while (deque.length && nums[deque[deque.length - 1]] < nums[right]) {
      deque.pop();
    }
    // console.log({ right, deque, val: nums[right] });
    deque.push(right);
    //! remove the left value from deque
    if (0 > deque[0]) {
      deque.shift();
    }
    //! add the max value to output
    if (right + 1 >= k) {
      output.push(nums[deque[0]]);
    }
    right++;
  }
  return output;


};

console.log(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3));

//! solution 2

const maxSlidingWindow2 = (nums, k) => {
  const res = [];
  const deque = [];
  let max = 0;
  for (let i = 0; i <= nums.length; i++) {
    if (deque.length !== k) {
      deque.push(nums[i]);
      max = Math.max(max, nums[i]);
    } else {
      let pop = deque.shift();
      max -= pop;
      res.push(max);
      deque.push(nums[i]);
    }
  }
  return res;
};

console.log(maxSlidingWindow2([1, 3, -1, -3, 5, 3, 6, 7], 3));




