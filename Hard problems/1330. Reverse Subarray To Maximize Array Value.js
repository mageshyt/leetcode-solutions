`You are given an integer array nums. The value of this array is defined as the sum of |nums[i] - nums[i + 1]| for all 0 <= i < nums.length - 1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.

 

Example 1:

Input: nums = [2,3,1,5,4]
Output: 10
Explanation: By reversing the subarray [3,1,5] the array becomes [2,5,1,3,4] whose value is 10.
Example 2:

Input: nums = [2,4,9,24,2,1,10]
Output: 68
 `;
const maxValueAfterReverse = (nums) => {
  let secondMax = -Infinity; //! because it will max when we compar with any number so we making it as negative infinity
  let secondMin = Infinity;
  let reverseVal = 0;
  const len = nums.length;
  let imp = 0;
  for (let i = 0; i < len - 1; i++) {
    const currDiff = Math.abs(nums[i] - nums[i + 1]); //! current different
    // console.log(currDiff);
    reverseVal += currDiff; //! reverse value
    console.log({ imp, secondMax, secondMin, currDiff, reverseVal });
    imp = Math.max(imp, Math.abs(nums[i + 1] - nums[0]) - currDiff); //!reverse 0 to i
    imp = Math.max(imp, Math.abs(nums[i] - nums[len - 1]) - currDiff); //!reverse i to len-1
    secondMax = Math.max(secondMax, Math.min(nums[i], nums[i + 1]));
    secondMin = Math.min(secondMin, Math.max(nums[i], nums[i + 1]));
  }
  console.log({ secondMax, secondMin, imp, reverseVal });
  return reverseVal + Math.max(imp, 2 * (secondMax - secondMin));
};
console.log(maxValueAfterReverse([2, 3, 1, 5, 4]));
