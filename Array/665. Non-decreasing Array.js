`Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).

 

Example 1:

Input: nums = [4,2,3]
Output: true
Explanation: You could modify the first 4 to 1 to get a non-decreasing array.
Example 2:

Input: nums = [4,2,1]
Output: false
Explanation: You can't get a non-decreasing array by modify at most one element.`;

const checkPossibility = (nums) => {
  let change_state = false;
  for (let i = 0; i < nums.length - 1; i++) {
    const current = nums[i];
    const next = nums[i + 1];
    if (current <= next) continue;

    if (change_state) return false;

    const prev = nums[i - 1];
    if (i === 0 || next >= prev) nums[i] = next;
    else nums[i + 1] = current;

    change_state = true;
  }
  return true;
};

console.log(checkPossibility([4, 2, 3]));
console.log(checkPossibility([4, 2, 1]));
