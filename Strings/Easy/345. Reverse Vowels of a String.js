`Given a string s, reverse only all the vowels in the string and return it.

The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.

 

Example 1:

Input: s = "hello"
Output: "holle"
Example 2:

Input: s = "leetcode"
Output: "leotcede"
 `;

var reverseVowels = function (s) {
  let left = 0;
  let right = s.length - 1;
  const vowels = "aeiouAEIOU";
  s = s.split("");
  while (left < right) {
    const curr = s[left];
    const last = s[right];
    console.log(curr, last);
    if (vowels.includes(curr) && vowels.includes(last)) {
      //! swap the letters
      [s[left], s[right]] = [s[right], s[left]];
      left++;
      right--;
    } else if (vowels.includes(curr)) {
      right--;
    } else if (vowels.includes(last)) {
      left++;
    } else {
      left++;
      right--;
    }
  }
  return s.join("");
};

console.log(reverseVowels("leetcode"));
