`You are given an integer array nums that is sorted in non-decreasing order.

Determine if it is possible to split nums into one or more subsequences such that both of the following conditions are true:

Each subsequence is a consecutive increasing sequence (i.e. each integer is exactly one more than the previous integer).
All subsequences have a length of 3 or more.
Return true if you can split nums according to the above conditions, or false otherwise.

A subsequence of an array is a new array that is formed from the original array by deleting some (can be none) of the elements without disturbing the relative positions of the remaining elements. (i.e., [1,3,5] is a subsequence of [1,2,3,4,5] while [1,3,2] is not).

 

Example 1:

Input: nums = [1,2,3,3,4,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,5] --> 1, 2, 3
[1,2,3,3,4,5] --> 3, 4, 5
Example 2:

Input: nums = [1,2,3,3,4,4,5,5]
Output: true
Explanation: nums can be split into the following subsequences:
[1,2,3,3,4,4,5,5] --> 1, 2, 3, 4, 5
[1,2,3,3,4,4,5,5] --> 3, 4, 5
Example 3:

Input: nums = [1,2,3,4,4,5]
Output: false
Explanation: It is impossible to split nums into consecutive increasing subsequences of length 3 or more.
`;

const isPossible = (nums) => {
  const map = new Map(); // map of number to number of times it appears in the array

  for (let num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  }

  const subSec = {}; // map of number to number of times it appears in the subsequence
  for (let num of nums) {
    subSec[num] = 0;
  }

  for (let num of nums) {
    if (!map.has(num)) continue; // if the number is not in the array, continue

    if (subSec[num - 1] > 0) {
      subSec[num - 1]--;
      subSec[num]++;
    } else {
      if (!map.has(num + 1) || !map.has(num + 2)) return false; // if the number is not in the array, continue
      map.set(num + 1, map.get(num + 1) - 1);
      map.set(num + 2, map.get(num + 2) - 1);
      subSec[num + 2]++;
    }
    map.set(num, map.get(num + 1) - 1);
  }
  return true;
};
console.log(isPossible([1, 2, 3, 3, 4, 5]));
console.log(isPossible([1, 2, 3, 3, 4, 4, 5, 5]));
console.log(isPossible([1, 2, 3, 4, 4, 5]));
