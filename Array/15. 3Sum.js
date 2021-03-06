`Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Example 2:

Input: nums = []
Output: []
Example 3:

Input: nums = [0]
Output: []
 `;

const threeSum = (nums) => {
  let ans = [];
  nums.sort((a, b) => a - b); // sort the array
  for (let i = 0; i < nums.length; i++) {
    const curr = nums[i];
    //! if not first value and curr=== nums[i-1] means we no need to use the same value again
    if (i > 0 && curr === nums[i - 1]) continue;
    let left = i + 1;
    let right = nums.length - 1;
    while (left < right) {
      const sum = curr + nums[left] + nums[right];
      if (sum === 0) {
        //! if our target is founded then push it to the ans array
        ans.push([curr, nums[left], nums[right]]);
        left += 1;
        //! if the left is equal to prev nums then we need to increment the left pointer
        while (nums[left] === nums[left - 1] && left < right) {
          left++;
        }
      }

      if (sum < 0) {
        left++;
      } else {
        right--;
      }
    }
  }
  return ans;
};

console.log(threeSum([-1, 0, 1, 2, -1, -4]));
