`Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
`;
const topKFrequent = (nums, k) => {
  const map = new Map(); //! map to count the frequency of the number
  for (let num of nums) {
    map.set(num, map.get(num) + 1 || 1);
  }
  const result = [];
  for (let [key, value] of map) {
    result.push([key, value]); //! we will add the number and its frequency
  }
  // result.sort((a, b) => b[1] - a[1]); //! we will solve with respect to the frequency of the number
  return result.slice(0, k).map((x) => x[0]); //! we will slice the list with respect to length of k
};
console.log(topKFrequent([1, 1, 1, 2, 2, 3], 2));
