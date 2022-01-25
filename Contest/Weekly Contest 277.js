`Given an integer array nums, return the number of elements that have both a strictly smaller and a strictly greater element appear in nums.

 

Example 1:

Input: nums = [11,7,2,15]
Output: 2
Explanation: The element 7 has the element 2 strictly smaller than it and the element 11 strictly greater than it.
Element 11 has element 7 strictly smaller than it and element 15 strictly greater than it.
In total there are 2 elements having both a strictly smaller and a strictly greater element appear in nums.`;

const countElements = (nums) => {
  let count = 0; // ! which help to count number has strictly greater element and strictly smaller
  let nums_length = nums.length;
  const max = Math.max(...nums); // ! max from the array

  const min = Math.min(...nums); // ! min from the array
  for (let i = 0; i < nums_length; i++) {
    if (nums[i] < max && nums[i] > min) {
      console.log("number satisfying the condition 😃", nums[i]);
      count++;
    }
  }

  return count;
};
nums = [11, 7, 2, 15];
console.log(countElements(nums));

`You are given a 0-indexed integer array nums of even length consisting of an equal number of positive and negative integers.

You should rearrange the elements of nums such that the modified array follows the given conditions:

Every consecutive pair of integers have opposite signs.
For all integers with the same sign, the order in which they were present in nums is preserved.
The rearranged array begins with a positive integer.
Return the modified array after rearranging the elements to satisfy the aforementioned conditions.

 

Example 1:

Input: nums = [3,1,-2,-5,2,-4]
Output: [3,-2,1,-5,2,-4]
Explanation:
The positive integers in nums are [3,1,2]. The negative integers are [-2,-5,-4].
The only possible way to rearrange them such that they satisfy all conditions is [3,-2,1,-5,2,-4].
Other ways such as [1,-2,2,-5,3,-4], [3,1,2,-2,-5,-4], [-2,3,-5,1,-4,2] are incorrect because they do not satisfy one or more conditions.  `;

const rearrangeArray = (nums) => {
  let nums_length = nums.length;
  let positive_nums = [[], []];
  let result = [];
  for (let i = 0; i < nums_length; i++) {
    if (nums[i] > 0) {
      positive_nums[0].push(nums[i]);
    } else {
      positive_nums[1].push(nums[i]);
    }
  }
  let positive_nums_length = positive_nums[0].length;
  let negative_nums_length = positive_nums[1].length;
  for (let i = 0; i < positive_nums_length; i++) {
    result.push(positive_nums[0][i]);
    result.push(positive_nums[1][i]);
  }
  return result;
};
nums = [3, 1, -2, -5, 2, -4];
// console.log(rearrangeArray(nums));

`You are given an integer array nums. A number x is lonely when it appears only once, and no adjacent numbers (i.e. x + 1 and x - 1) appear in the array.

Return all lonely numbers in nums. You may return the answer in any order.

 

Example 1:

Input: nums = [10,6,5,8]
Output: [10,8]
Explanation: 
- 10 is a lonely number since it appears exactly once and 9 and 11 does not appear in nums.
- 8 is a lonely number since it appears exactly once and 7 and 9 does not appear in nums.
- 5 is not a lonely number since 6 appears in nums and vice versa.
Hence, the lonely numbers in nums are [10, 8].
Note that [8, 10] may also be returned.
Example 2:

Input: nums = [1,3,5,3]
Output: [1,5]
Explanation: 
- 1 is a lonely number since it appears exactly once and 0 and 2 does not appear in nums.
- 5 is a lonely number since it appears exactly once and 4 and 6 does not appear in nums.
- 3 is not a lonely number since it appears twice.
Hence, the lonely numbers in nums are [1, 5].
Note that [5, 1] may also be returned.`;

const lonelyNumbers = (nums) => {
  const result = [];
  const nums_length = nums.length;
  const nums_set = {};
  for (let i = 0; i < nums_length; i++) {
    const current = nums[i];
    if (current in nums_set) {
      nums_set[current] = nums_set[current] + 1;
    } else {
      nums_set[current] = 1;
    }
  }
  for (let i = 0; i < nums_length; i++) {
    const current = nums[i];
    if (
      nums_set[current] === 1 &&
      !(current + 1 in nums_set) &&
      !(current - 1 in nums_set)
    ) {
      result.push(current);
    }
  }
  return result;
};
nums = [10, 6, 5, 8];
// console.log(lonelyNumbers(nums));
