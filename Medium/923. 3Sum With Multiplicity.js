`Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.
Example 2:

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
Explanation: 
arr[i] = 1, arr[j] = arr[k] = 2 occurs 12 times:
We choose one 1 from [1,1] in 2 ways,
and two 2s from [2,2,2,2] in 6 ways.`;

const threeSumMulti = (arr, target) => {
  let mod = 1e9 + 7;
  const dp = new Array(300).fill(0);
  let ans = 0;
  for (let i = 0; i < arr.length; i++) {
    ans += target - arr[i] >= 0 ? dp[target - arr[i]] : 0;
    console.log({ ans, res: target - arr[i] });
    ans %= Math.pow(10, 9) + 7;
    // console.log({ modans: ans });
    for (let j = 0; j < i; j++) {
      dp[arr[i] + arr[j]]++;
    //   console.log({ dp: dp[arr[i] + arr[j]], idx: arr[i] + arr[j] });
    }
  }
  return ans % mod;
};
console.log(threeSumMulti([1, 1, 2, 2, 3, 3, 4, 4, 5, 5], 8));
