`Given an integer array nums, return the number of longest increasing subsequences.

Notice that the sequence has to be strictly increasing.

 

Example 1:

Input: nums = [1,3,5,4,7]
Output: 2
Explanation: The two longest increasing subsequences are [1, 3, 4, 7] and [1, 3, 5, 7].
Example 2:

Input: nums = [2,2,2,2,2]
Output: 5
Explanation: The length of longest continuous increasing subsequence is 1, and there are 5 subsequences' length is 1, so output 5.
`;

const findNumberOfLIS = (nums) => {
  const dp = new Map(); // ! key=index and value =[length, count]
  let maxLIS = 0;
  let res = 0;

  for (let i = nums.length; i > 0; i--) {
    //! max len and max count
    let [maxLen, maxCount] = [1, 1]; //! because we assume that the first element is the longest increasing subsequence
    for (let j = i + 1; j < nums.length; j++) {
      //! to make sure that we are in increasing orderS
      if (nums[i] < nums[j]) {
        const [length, count] = dp.get(j);

        if (length + 1 > maxLen) {
          maxLen = length + 1;
          maxCount = count;
        } else if (length + 1 === maxLen) {
          maxCount += count;
        }
      }
    }
    if (maxLen > maxLIS) {
      maxLIS = maxLen;
      res = maxCount;
    } else if (maxLen === maxLIS) {
      res += maxCount;
    }
    dp.set(i, [maxLen, maxCount]);
  }
  return res;
};
console.log(findNumberOfLIS([1, 3, 5, 4, 7]));
