`Given four integer arrays nums1, nums2, nums3, and nums4 all of length n, return the number of tuples (i, j, k, l) such that:

0 <= i, j, k, l < n
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
 

Example 1:

Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
Output: 2
Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0`;

const fourSumCount = (nums1, num2, num3, num4) => {
  const hash = {};

  for (let i = 0; i < nums1.length; i++) {
    const current = nums1[i];
    for (let j = 0; j < num2.length; j++) {
      const current2 = num2[j];
      const sum = current + current2;
      if (!hash[sum]) {
        hash[sum] = 1;
      } else {
        hash[sum]++;
      }
    }
  }
  let count = 0;
  //   console.log(hash);
  for (let i = 0; i < num3.length; i++) {
    for (let j = 0; j < num4.length; j++) {
      const target = -(num3[i] + num4[j]);
      if (hash[target]) {
        count += hash[target];
      }
    }
  }
  return count;
};

console.log(fourSumCount([-1, -1], [-1, 1], [-1, 1], [1, -1]));
