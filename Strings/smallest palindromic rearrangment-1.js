`
You are given a palindromic string s.

Return the lexicographically smallest palindromic permutation of s.

 

Example 1:

Input: s = "z"

Output: "z"

Explanation:

A string of only one character is already the lexicographically smallest palindrome.

Example 2:

Input: s = "babab"

Output: "abbba"

Explanation:

Rearranging "babab" → "abbba" gives the smallest lexicographic palindrome.

Example 3:

Input: s = "daccad"

Output: "acddca"

Explanation:

Rearranging "daccad" → "acddca" gives the smallest lexicographic palindrome.
`

const smallestPalindrom = (s) => {
  const n = s.length;
  // base case : if the string is empty or has only one character, return it
  if (n === 1) return s;

  const freq = new Map();

  for(let char of s){
    freq.set(char, (freq.get(char) || 0) + 1);
  }

  // find the middle character
  let midChar = '';
  let oddCount = 0;

  for (let [char, count] of freq) {
    if (count % 2 === 1) {
      oddCount++;
      midChar = char;
    }
  }

  if (oddCount > 1) return '';

  // create the left half of the palindrome
  let leftHalf = '';
  for (let [char, count] of freq) {
    leftHalf += char.repeat(Math.floor(count / 2));
  }

  leftHalf = leftHalf.split('').sort().join('');

  // create the right half by reversing the left half

  let rightHalf = leftHalf.split('').reverse().join('');
  // if there is a middle character, add it to the palindrome
  return leftHalf + (midChar ? midChar : '') + rightHalf;

}
console.log(smallestPalindrom('z')); // Output: "z"
console.log(smallestPalindrom('babab')); // Output: "abbba"
console.log(smallestPalindrom('daccad')); // Output: "acddca"
