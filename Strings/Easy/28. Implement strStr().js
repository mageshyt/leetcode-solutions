`
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 
if needle is not part of haystack.

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. 
This is consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
`;

const firstOccurrence = (haystack, needle) => {
  // ! Edge case
  if (needle.length === 0) return 0;
  if (haystack.length === 0) return -1;
  // needle length need to be less than  haystack length
  if (needle.length > haystack.length) return -1;
  for (let i = 0; i < haystack.length; i++) {
    if (haystack[i] === needle[0]) {
      const sp = haystack.slice(i, i + needle.length);
      if (sp === needle) return i;
    }
  }
  return -1;
};

console.log(firstOccurrence("mississippi", "issip"));
("mississippi");
