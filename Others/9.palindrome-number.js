/*
 * @lc app=leetcode id=9 lang=javascript
 *
 * [9] Palindrome Number
 */

// @lc code=start
/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function (x) {
  let reverse = 0;
  const a = x;
  while (x > 0) {
    reverse = reverse * 10 + (x % 10);
    x = parseInt(x / 10);
  }
  //   console.log(a);
  if (a === reverse) {
    return true;
  } else {
    return false;
  }
};
// @lc code=end
isPalindrome(121);
