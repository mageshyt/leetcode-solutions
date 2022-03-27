`Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
`;

const findDuplicate = (nums) => {
  let slow = nums[0];
  let fast = nums[nums[0]];
  // where are finding the meeting point
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[nums[fast]];
    console.log({ slow, fast });
  }
  slow = 0;
  while (slow !== fast) {
    slow = nums[slow];
    fast = nums[fast];
  }
  return slow;
};

const findDuplicate2 = (nums) => {
  let lef = 0;
  let right = 1;
  nums.sort((a, b) => a - b);
  while (lef < right) {
    const left_curr = nums[lef];
    const right_curr = nums[right];
    if (left_curr === right_curr) {
      return left_curr;
    }
    lef += 1;
    right += 1;
  }
};
console.log(findDuplicate([1, 3, 4, 2, 2]));
