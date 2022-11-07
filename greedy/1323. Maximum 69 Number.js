`You are given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).

 

Example 1:

Input: num = 9669
Output: 9969
Explanation: 
Changing the first digit results in 6669.
Changing the second digit results in 9969.
Changing the third digit results in 9699.
Changing the fourth digit results in 9666.
The maximum number is 9969.
Example 2:

Input: num = 9996
Output: 9999
Explanation: Changing the last digit 6 to 9 results in the maximum number.
Example 3:

Input: num = 9999
Output: 9999
Explanation: It is better not to apply any change.`;
const maximum69Number = (num) => {
  const numArray = num
    .toString()
    .split("")
    .map((ele) => parseInt(ele));
  let count_6 = 1;
  let count_9 = 1;
  let res = num;
  for (let index = 0; index < numArray.length; index++) {
    if (count_9 == 0 && count_6 == 0) break;
    if (numArray[index] == 6) {
      let temp = numArray[index];
      numArray[index] = 9;
      if (Number(numArray.join("")) > res && count_6 > 0) {
        res = Number(numArray.join(""));
        count_6--;
      } else {
        numArray[index] = temp;
      }
    } else if (numArray[index] == 9) {
      
      let temp = numArray[index];
      numArray[index] = 6;
      if (Number(numArray.join("")) > res && count_9 > 0) {
        res = Number(numArray.join(""));
        count_9--;
      } else {
        numArray[index] = temp;
      }
    }
  }
  return res;
};
console.log(maximum69Number(9669));
console.log(maximum69Number(9996));
console.log(maximum69Number(9999));
