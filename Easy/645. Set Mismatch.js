`You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
`;
const findErrorNums = (nums) => {
  let missing;
  let duplicate;
  let len = nums.length;
  nums.sort((a, b) => a - b);
  for (let i = 0; i < len; i++) {
    const curr = nums[i];
    const next = nums[i + 1];
    if (curr === next) {
      duplicate = curr;
      break;
    }
  }
  for (let i = 1; i <= len; i++) {
    if (nums.indexOf(i) === -1) {
      missing = i;
      break;
    }
  }
  return [duplicate, missing];
};
console.log(findErrorNums([1, 2, 2, 4]));
console.log(findErrorNums([2, 3, 2]));
