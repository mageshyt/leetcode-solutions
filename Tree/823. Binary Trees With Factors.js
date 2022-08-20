`Given an array of unique integers, arr, where each integer arr[i] is strictly greater than 1.

We make a binary tree using these integers, and each number may be used for any number of times. Each non-leaf node's value should be equal to the product of the values of its children.

Return the number of binary trees we can make. The answer may be too large so return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [2,4]
Output: 3
Explanation: We can make these trees: [2], [4], [4, 2, 2]
Example 2:

Input: arr = [2,4,5,10]
Output: 7
Explanation: We can make these trees: [2], [4], [5], [10], [4, 2, 2], [10, 2, 5], [10, 5, 2].
 `;

const numFactoredBinaryTrees = (arr) => {
  arr.sort((a, b) => a - b);

  const map = {};

  const mod = 10 ** 9 + 7;
  for (let num of arr) {
    map[num] = 1;
  }
  for (let i = 0; i < arr.length; i++) {
    const curr = arr[i];
    for (let j = 0; j < i; j++) {
      if (!(curr % arr[j]) && Math.floor(curr / arr[j]) in map) {
        map[curr] += map[arr[j]] * map[Math.floor(curr / arr[j])];
        map[curr] %= mod;
      }
    }
  }

  const result = Object.values(map).reduce((a, b) => a + b, 0);
  return result % mod;
};

console.log(numFactoredBinaryTrees([2, 4]));
