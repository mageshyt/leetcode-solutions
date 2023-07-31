`Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

 

Example 1:

Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
Example 2:

Input: s1 = "delete", s2 = "leet"
Output: 403
Explanation: Deleting "dee" from "delete" to turn the string into "let",
adds 100[d] + 101[e] + 101[e] to the sum.
Deleting "e" from "leet" adds 101[e] to the sum.
At the end, both strings are equal to "let", and the answer is 100+101+101+101 = 403.
If instead we turned both strings into "lee" or "eet", we would get answers of 433 or 417, which are higher.
 `;

const minimumDeleteSum = (s1, s2) => {
  const cache = new Map();
  const len1 = s1.length;
  const len2 = s2.length;

  const dp = (i, j) => {
    //  if both are in the end of the string [no need to delete]
    if (i == len1 && j == len2) return 0;

    // if we reach the end of s1 [delete all the rest of s2]

    if (i == len1) return sumOfAscii(s2.slice(j));

    // if we reach the end of s2 [delete all the rest of s1]

    if (j == len2) return sumOfAscii(s1.slice(i));

    const key = `${i}-${j}`;

    if (cache.has(key)) return cache.get(key);

    let res = 0;

    // if both are equal [no need to delete so move to the next char]

    if (s1[i] == s2[j]) {
      res = dp(i + 1, j + 1);
    } else {
      // if both are not equal [delete one of them and move to the next char]
      res = Math.min(
        s1.charCodeAt(i) + dp(i + 1, j), // delete s1[i]
        s2.charCodeAt(j) + dp(i, j + 1) // delete s2[j]
      );
    }
    cache.set(key, res);

    return res;
  };

  return dp(0, 0);
};

const sumOfAscii = (str) => {
  let sum = 0;
  for (let i = 0; i < str.length; i++) {
    sum += str.charCodeAt(i);
  }
  return sum;
};

console.log("👉 result ", minimumDeleteSum("delete", "leet"));

// console.log("👉 result ", sumOfAscii("leet"));
