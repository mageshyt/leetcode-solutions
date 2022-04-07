`1.Median of Two Sorted Arrays
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
`;
// solution 1

const medianArrays = (nums1, nums2) => {
  const merged = [...nums1, ...nums2].sort((a, b) => a - b); // add the two arrays and sort them
  const len = merged.length; // length of the merged array
  if (len % 2 === 0) {
    return (merged[len / 2 - 1] + merged[len / 2]) / 2;
  }
  // for odd number return the middle element
  return merged[(len - 1) / 2];
};

// console.log(medianArrays([1, 2], [3, 4]));

// solution 2

const mergedArrays2 = (nums1, nums2) => {
  let A = nums1;
  let B = nums2;
  let total = nums1.length + nums2.length; // total length of the merged array
  let half = Math.floor(total / 2); // half length of the merged array

  if (A.length > B.length) {
    [A, B] = [B, A]; // swap A and B
  }
  let left = 0;
  let right = A.length - 1;
  while (true) {
    i = Math.floor((left + right) / 2); // for array A

    j = half - i - 2; // for array B
    // Array A
    ALeft = i >= 0 ? A[i] : -Infinity; // left bound of A
    ARight = i + 1 < A.length ? A[i + 1] : Infinity; // right bound of A
    // Array B
    BLeft = j >= 0 ? B[j] : -Infinity; // left bound of B
    BRight = j + 1 < B.length ? B[j + 1] : Infinity; // right bound of B
    // partition check
    if (ALeft <= BRight && BLeft <= ARight) {
      // there are 2 conditions to check:
      // 1.Odd number
      // 2. Even number

      // if odd then return the middle element
      if (total % 2) {
        return A[i];
      }
      // if it is even then add max of left and min of right
      return Math.max(ALeft, BLeft) + Math.min(ARight, BRight) / 2;
    } else if (ALeft > BRight) {
      right = i - 1;
    } else {
      left = i + 1;
    }
  }
};
console.log(mergedArrays2([1, 2], [3]));

// problem 2
`Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.
`;

const search = (nums, target) => {
  let left = 0;
  let right = nums.length - 1;
  while (left <= right) {
    let mid = Math.floor((left + right) / 2);
    if (nums[mid] === target) {
      return mid;
    } else if (nums[mid] < target) {
      left = mid + 1;
    } else {
      right = mid - 1;
    }
  }
  return -1;
};
