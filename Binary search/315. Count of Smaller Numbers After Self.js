`You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

 

Example 1:

Input: nums = [5,2,6,1]
Output: [2,1,1,0]
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
Example 2:

Input: nums = [-1]
Output: [0]
Example 3:

Input: nums = [-1,-1]
Output: [0,0]
 `;
const BinarySearch = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;
  while (left <= right) {
    const mid = Math.floor((left + right) / 2);
    if (nums[mid] < target) left = mid + 1;
    else right = mid - 1;
  }
  return left;
};

const countSmaller = (nums) => {
  const result = [];
  const sorted = [...nums].sort((a, b) => a - b);

  for (let i = 0; i < nums.length - 1; i++) {
    const index = BinarySearch(sorted, nums[i]);
    sorted.splice(index, 1);
    result.push(index);
  }
  result.push(0);
  return result;
};
console.log(countSmaller([5, 2, 6, 1]));
console.log(countSmaller([-1]));
console.log(countSmaller([-1, -1]));
