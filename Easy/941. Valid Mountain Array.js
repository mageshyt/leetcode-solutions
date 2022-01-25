`Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

Example 1:

Input: arr = [2,1]
Output: false
Example 2:

Input: arr = [3,5,5]
Output: false
Example 3:

Input: arr = [0,3,2,1]
Output: true`;

const validMountainArray = (arr) => {
  let strictly_increasing_and_decreasing = 0;
  for (let i = 1; i <= arr.length - 1; i++) {
    const current = arr[i];
    const next = arr[i + 1];
    const prev= arr[i-1];
    if (current === next) return false;
    if (current < next && current < prev) {
        return false;
    } else if (current > next && current > prev) {
        strictly_increasing_and_decreasing++;
    }
  }
};
arr = [0, 3, 2, 1];
console.log(validMountainArray(arr));
