`Given a list of unique words, return all the pairs of the distinct indices (i, j) in the given list, so that the\
 concatenation of the two words words[i] + words[j] is a palindrome.
 Example 1:

Input: words = ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]]
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]
Example 2:

Input: words = ["bat","tab","cat"]
Output: [[0,1],[1,0]]
Explanation: The palindromes are ["battab","tabbat"]
Example 3:

Input: words = ["a",""]
Output: [[0,1],[1,0]]`;

const isPalindrome = (word) => {
  const res = new Set();
  const map = new Map();

  for (let i = 0; i < word.length; i++) {
    map.set(word[i], i);
  }

  for (let i = 0; i < word.length; i++) {
    //! if empty string is present then continue
    if (!word[i]) continue;

    // Possible palindrome in LHS
    for (let j = 0; j < word.length; j++) {
      const left = word[i].substring(0, j);
      const needed = word[i].substring(j).split("").reverse().join("");

      const leftReverse = left.split("").reverse().join("");
      if (left === leftReverse && needed !== word[i] && map.has(needed)) {
        res.add([map.get(needed), i]);
      }
    }

    //! possible palindrome in RHS

    for (let j = word[i].length - 1; j >= 0; j--) {
      const right = word[i].substring(j);
      const needed = word[i].substring(0, j).split("").reverse().join("");
      const rightReverse = right.split("").reverse().join("");
      if (right === rightReverse && needed !== word[i] && map.has(needed)) {
        res.add([i, map.get(needed)]);
      }
    }

    if (word[i] === word[i].split("").reverse().join("") && map.has("")) {
      res.add([i, map.get("")]);
      res.add([map.get(""), i]);
    }
  }
  const result = new Map();
  for (let pairs of [...res]) {
    const key = pairs[0] + "," + pairs[1];
    result.set(key, pairs);
  }
  return [...result.values()];
};

const checkPalindrome = (word) => {
  let i = 0;
  let j = word.length - 1;
  while (i < j) {
    if (word[i] !== word[j]) {
      return false;
    }
    i++;
    j--;
  }
  return true;
};

console.log(isPalindrome(["abcd", "dcba", "lls", "s", "sssll"]));
console.log(isPalindrome(["bat", "tab", "cat"]));
console.log(isPalindrome(["a", ""]));
