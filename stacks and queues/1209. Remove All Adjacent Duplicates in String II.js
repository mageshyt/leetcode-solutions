`You are given a string s and an integer k, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them, causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It is guaranteed that the answer is unique.

 

Example 1:

Input: s = "abcd", k = 2
Output: "abcd"
Explanation: There's nothing to delete.
Example 2:

Input: s = "deeedbbcccbdaa", k = 3
Output: "aa"
Explanation: 
First delete "eee" and "ccc", get "ddbbbdaa"
Then delete "bbb", get "dddaa"
Finally delete "ddd", get "aa"
Example 3:

Input: s = "pbbcggttciiippooaais", k = 2
Output: "ps"`;

const removeDuplicates = (S, K) => {
  const map = new Map();
  let count = 0;
  let result = "";
  for (let i = 0; i < S.length; i++) {
    map.set(S[i], map.get(S[i]) + 1 || 1);
  }
  for (let [key, val] of map.entries()) {
    if (val % K === 0) {
      map.set(key, val % K);
      count++;
    } else {
      result += key;
    }
  }

  for (let [key, val] of map.entries()) {
    if (val % K === 0) {
      map.set(key, val % K);
    } else {
      result += key;
    }
  }
  return result;
};
console.log(removeDuplicates("pbbcggttciiippooaais", 2));

console.log(removeDuplicates("abcd", 2));

console.log(removeDuplicates("deeedbbcccbdaa", 3));
