`The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
 

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
Example 3:

Input: s = "A", numRows = 1
Output: "A"`;

const convert = (s, numRows) => {
  //!edge case
  if (numRows === 1) return s;
  let final_reduced = "";
  for (let row = 0; row < numRows; row++) {
    let increment = 2 * (numRows - 1); // distance we jump each time
    for (let i = row; i < s.length; i += increment) {
      final_reduced += s[i]; // this is work perfectly for first and last row

      // for middle rows
      const middleRowCheck = row > 0 && row < numRows - 1;
      const outOfBounds = i + increment * 2 - row < s.length;
      if (middleRowCheck && outOfBounds) {
        final_reduced += s[i + increment - 2 * row];
        console.log(s[(i + increment) * 2 - row], final_reduced);
      }
    }
  }
  return final_reduced;
};

console.log(convert("PAYPALISHIRING", 3));
