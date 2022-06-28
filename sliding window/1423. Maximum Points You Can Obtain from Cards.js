`There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array cardPoints.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly k cards.

Your score is the sum of the points of the cards you have taken.

Given the integer array cardPoints and the integer k, return the maximum score you can obtain.

 

Example 1:

Input: cardPoints = [1,2,3,4,5,6,1], k = 3
Output: 12
Explanation: After the first step, your score will always be 1. However, choosing the rightmost card first will maximize your total score. The optimal strategy is to take the three cards on the right, giving a final score of 1 + 6 + 5 = 12.
Example 2:

Input: cardPoints = [2,2,2], k = 2
Output: 4
Explanation: Regardless of which two cards you take, your score will always be 4.
Example 3:

Input: cardPoints = [9,7,7,9,7,7,9], k = 7
Output: 55
Explanation: You have to take all the cards. Your score is the sum of points of all cards.
 `;

const sum = (nums) => {
  return nums.reduce((num, acc) => num + acc, 0);
};

const maxScore = (nums, k) => {
  const len = nums.length;
  let total = sum(nums); //! total of the array
  let window_sum = 0; //! to find the min subarray sum of length n-k
  let window_start = 0; 
  for (let i = 0, curr_sum = 0; i < len; i++) {
    curr_sum += nums[i];
    console.log({ curr_sum, diff: len - k, i, window_sum });
    if (i < len - k) {
      window_sum += nums[i];
    } else {
      //! when our window get large than n-k then we have to shift the window 
      console.log("lol");
      curr_sum -= nums[window_start];
      window_start++;
      window_sum = Math.min(window_sum, curr_sum);
    }
  }
  return total - window_sum;
};

const cardPoints = [100, 40, 17, 9, 73, 75];
k = 3;
console.log(maxScore(cardPoints, k));
