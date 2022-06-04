`Given a string s, you can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. Return the output in any order.

 

Example 1:

Input: s = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]
Example 2:

Input: s = "3z4"
Output: ["3z4","3Z4"]`;

const letterCasePermutation = (s) => {
  let res = [];
  const backtracking = (str, index) => {
    if (s.length === index) {
      res.push(str);
      return;
    }
    //! if it is a letter
    if (s[index].match(/[a-zA-Z]/)) {
      backtracking(str + s[index].toUpperCase(), index + 1);
      backtracking(str + s[index].toLowerCase(), index + 1);
    } else {
      backtracking(str + s[index], index + 1);
    }
  };
  backtracking("", 0);
  return res;
};

console.log(letterCasePermutation("a1b2"));
