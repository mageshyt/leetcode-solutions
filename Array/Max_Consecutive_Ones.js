`
Given a binary array nums, return the maximum number of consecutive 1's in the array.

 

Example 1:

Input: nums = [1,1,0,1,1,1]
Output: 3
Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
`;
const consecutiveOnes = (array) => {
  let max = 0;
  for (let i = 0; i <= array.length; i++) {
    const current = array[i];
    if (current === 1) {
      //   console.log({ i, current });
      let count = 1;
      for (let j = i + 1; j <= array.length; j++) {
        // console.log({ j, i, current: array[j], count });
        if (array[j] === 1) {
          count++;
        } else if (array[j] === 0) {
          break;
        }
      }
      max = Math.max(max, count);
    }
  }
  return max;
};
const nums = [1, 1, 0, 1, 1, 1];
console.log(consecutiveOnes(nums));
