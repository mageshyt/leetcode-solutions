`Given an integer array nums, handle multiple queries of the following types:

Update the value of an element in nums.
Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
void update(int index, int val) Updates the value of nums[index] to be val.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
 

Example 1:

Input
["NumArray", "sumRange", "update", "sumRange"]
[[[1, 3, 5]], [0, 2], [1, 2], [0, 2]]
Output
[null, 9, null, 8]

Explanation
NumArray numArray = new NumArray([1, 3, 5]);
numArray.sumRange(0, 2); // return 1 + 3 + 5 = 9
numArray.update(1, 2);   // nums = [1, 2, 5]
numArray.sumRange(0, 2); // return 1 + 2 + 5 = 8
 

Constraints:

1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
0 <= index < nums.length
-100 <= val <= 100
0 <= left <= right < nums.length
At most 3 * 104 calls will be made to update and sumRange.`;

class NumArray {
  constructor(nums) {
    this.nums = nums;
    this.currSum = nums.reduce((a, b) => a + b);
    this.len = nums.length;
  }

  update(index, val) {
    this.currSum -= this.nums[index];
    this.nums[index] = val;
    this.currSum += val;
  }
  sumRange(left, right) {
    if (right - left > Math.floor(this.len / 2)) {
      const left_arr = this.nums.slice(0, left);
      left_arr.push(0);
      const right_arr = this.nums.slice(right + 1);

      const range_sum = left_arr.concat(right_arr).reduce((a, b) => a + b);

      return this.currSum - range_sum;
    } else {
      return this.nums.slice(left, right + 1).reduce((a, b) => a + b);
    }
  }
}

const sol = new NumArray([1, 3, 5]);
console.log(sol.sumRange(0, 2));
sol.update(1, 2);
console.log(sol.sumRange(0, 2));
