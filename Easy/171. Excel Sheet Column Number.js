`Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.
For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
`;

const titleToNumber = (columnTitle) => {
  let corresponding_number = 0;
  for (let i = 0; i < columnTitle.length; i++) {
    const current_letter = columnTitle[i]; // current Letter
    const current_number = current_letter.charCodeAt(0) - 64; // corresponding number 
    // here we are subtracting 64 because we aer going to get only Capital letter so t charCodeAt() returns the ASCII value of the character.
    corresponding_number +=
      current_number * Math.pow(26, columnTitle.length - i - 1);
  }
  return corresponding_number;
};

console.log(titleToNumber("A"));
console.log(titleToNumber("AB"));
console.log(titleToNumber("ZY"));
console.log(titleToNumber("CD"));
