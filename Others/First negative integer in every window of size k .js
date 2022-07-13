`iven an array A[] of size N and a positive integer K, find the first negative integer for each and every window(contiguous subarray) of size K.

 

Example 1:

Input : 
N = 5
A[] = {-8, 2, 3, -6, 10}
K = 2
Output : 
-8 0 -6 -6
Explanation :
First negative integer for each window of size k
{-8, 2} = -8
{2, 3} = 0 (does not contain a negative integer)
{3, -6} = -6
{-6, 10} = -6
 
Example 2:
Input : 
N = 8
A[] = {12, -1, -7, 8, -15, 30, 16, 28}
K = 3
Output :
-1 -1 -7 -15 -15 0 `;

function getNegative(nums) {
  for (let i = 0; i < nums.length; i++) {
    if (nums[i] < 0) {
      return nums[i];
    }
  }
  return 0;
}

const FirstNegativeIntegerInEveryWindowOfSizeK = (arr, k) => {
  const result = [];
  const window = [];

  let windowStart = 0;
  let windowEnd = 0;
  const len = arr.length;
  while (windowEnd <= len) {
    const current = arr[windowEnd];
    if (window.length === k) {
      result.push(getNegative(window));
      window.shift();
      windowStart++;
    } else {
      window.push(current);
    }

    windowEnd++;
  }
  return result;
};
console.log(FirstNegativeIntegerInEveryWindowOfSizeK([-8, 2, 3, -6, 10], 2));
console.log(
  FirstNegativeIntegerInEveryWindowOfSizeK([12, -1, -7, 8, -15, 30, 16, 28], 3)
);

const solution2 = (nums, k) => {
  let windowStart = 0;

  const result = [];
  const currWindow = [];

  for (let windowEnd = 0; windowEnd < nums.length; windowEnd++) {
    const current = nums[windowEnd];
    if (current < 0) {
      currWindow.push(current);
    }
    // console.log({ windowStart });
    const windowSize = windowEnd - windowStart + 1;
    if (windowSize === k) {
      if (currWindow.length === 0) {
        //! if there is no negative number in the window then push 0
        result.push(0);
      } else {
        result.push(currWindow[0]);
      }
      if (nums[windowStart] < 0) {
        //! if we have negative number in the window we need to remove it from the currWindow
        currWindow.shift();
      }
      windowStart++;
    }
  }
  return result;
};

// console.log(solution2([-8, 2, 3, -6, 10], 2));
// console.log(solution2([12, -1, -7, 8, -15, 30, 16, 28], 3));
