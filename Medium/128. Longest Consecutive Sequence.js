`Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9`;

//! sorting solution
const longestConsecutive = (nums) => {
  if (nums.length === 0) return 0;
  const hash = new Set(nums);
  let longest = 0;
  for (const num of nums) {
    if (!hash.has(num - 1)) {
      let current = num;
      while (hash.has(current)) {
        current++;
      }
      longest = Math.max(longest, current - num);
    }
  }
  return longest;
};
console.log(longestConsecutive([100, 4, 200, 1, 3, 2]));
1, 2, 3, 4;
