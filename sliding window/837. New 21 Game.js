`Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.

 

Example 1:

Input: n = 10, k = 1, maxPts = 10
Output: 1.00000
Explanation: Alice gets a single card, then stops.
Example 2:

Input: n = 6, k = 1, maxPts = 10
Output: 0.60000
Explanation: Alice gets a single card, then stops.
In 6 out of 10 possibilities, she is at or below 6 points.
Example 3:

Input: n = 21, k = 17, maxPts = 10
Output: 0.73278`;
const new21Game = (n, k, maxPts) => {
  // base case
  if (k === 0 || k + maxPts <= n) return 1;

  let windowSum = 0;
  // make 1 for value greater than k
  for (let i = k; i <= k + maxPts; i++) {
    windowSum += i <= n ? 1 : 0;
  }

  const dp = {};

  for (let i = k - 1; i >= 0; i--) {
    dp[i] = windowSum / maxPts;
    let remove = 0;
    if (i + maxPts <= n) {
      remove = dp[i + maxPts] || 1;
    }

    windowSum += dp[i] - remove; // add new and remove old
  }

  return dp[0];
};

console.log(new21Game(21, 17, 10));

// Path: sliding window/978. Longest Turbulent Subarray.js
