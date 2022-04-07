`Given an array nums of integers, return how many of them contain an even number of digits.

 

Example 1:

Input: nums = [12,345,2,6,7896]
Output: 2
Explanation: 
12 contains 2 digits (even number of digits). 
345 contains 3 digits (odd number of digits). 
2 contains 1 digit (odd number of digits). 
6 contains 1 digit (odd number of digits). 
7896 contains 4 digits (even number of digits). 
Therefore only 12 and 7896 contain an even number of digits.`;
const evenDigits = (array) => {
  let count = 0;
  for (let i = 0; i < array.length; i++) {
    let current = array[i];
    const convert_current = current.toString().split(""); // convert to string and check the length
    if (convert_current.length % 2 === 0) {
      count++;
    }
  }
  return count;
};
nums = [12, 345, 2, 6, 7896];
// console.log(evenDigits(nums));
// !---------------------------------------------------------------------------------------------------------------------
`Squares of a Sorted Array
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
`;

const squareSortedArray = (array) => {
  const new_array = array.map((num) => {
    return num * num;
  });
  return new_array.sort((a, b) => {
    return a - b;
  });
};
// console.log(squareSortedArray([-4, -1, 0, 3, 10]));
// !---------------------------------------------------------------------------------------------------------------------
`88. Merge Sorted Array
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

 

Example 1:

Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
`;

const mergeSortedArray = (nums1, m, nums2, n) => {
  let left = m - 1;
  let right = n - 1;

  for (let i = nums1.length - 1; i >= 0; i--) {
    if (right < 0) {
      break;
    }

    if (left >= 0 && nums1[left] > nums2[right]) {
      nums1[i] = nums1[left--];
    } else {
      nums1[i] = nums2[right--];
    }
  }
};
// console.log(mergeSortedArray([0, 0, 0, 0, 0], 0, [1, 2, 3, 4, 5], 5));
// !----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

`448. Find All Numbers Disappeared in an Array

Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

 

Example 1:

Input: nums = [4,3,2,7,8,2,3,1]
Output: [5,6]
Example 2:

Input: nums = [1,1]
Output: [2]
 `;

const findDisappearedNumbers = (nums) => {
  let new_array = [];
  for (let i = 1; i <= nums.length; i++) {
    if (!nums.includes(i)) {
      new_array.push(i);
    }
  }
  return new_array;
};

// console.log(findDisappearedNumbers([1, 1]));

//!----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
`Two sum ii
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.

 

Example 1:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].`;

const TwoSum = (numbers, target) => {
  const nums_map = {};

  for (let p = 0; p < nums.length; p++) {
    let current_Value = nums[p];
    if (nums_map[nums[p]] !== undefined) {
      return [nums_map[current_Value] + 1, p + 1];
    } else {
      nums_map[target - current_Value] = p;
    }
  }
};
nums = [2, 7, 11, 15];
target = 9;
console.log(TwoSum(nums, target));
