`A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

 

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.`;

const minFlipsMonoIncr = (s) => {
  let count = 0;
  let flip = 0;
  let idx_1 = -1;
  for (let i = 0; i < s.length; i++) {
    // find the first 1
    if (s[i] === "1") {
      idx_1 = i;
      break;
    }
  }

  // if there is no 1, return 0
  if (idx_1 === -1) return 0;
  for (let i = idx_1; i < s.length; i++) {
    // count no of 1's and no of 0's
    if (s[i] === "1") {
      count++;
    } else {
      flip++;
    }
    // if no of 0's > no of 1's, flip the 0 to 1
    flip = Math.min(flip, count);
  }

  return flip;
};
console.log("👉 Result: ", minFlipsMonoIncr("00110"));
console.log("👉 Result: ", minFlipsMonoIncr("010110"));
console.log("👉 Result: ", minFlipsMonoIncr("00011000"));
