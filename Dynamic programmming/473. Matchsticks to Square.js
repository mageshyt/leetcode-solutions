`ou are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must be used exactly one time.

Return true if you can make this square and false otherwise.

 

Example 1:


Input: matchsticks = [1,1,2,2,2]
Output: true
Explanation: You can form a square with length 2, one side of the square came two sticks with length 1.
Example 2:

Input: matchsticks = [3,3,3,3,4]
Output: false
Explanation: You cannot find a way to form a square with all the matchsticks.
`;

const makesquare = (matchsticks) => {
  const sum = matchsticks.reduce((a, b) => a + b, 0);

  if (sum % 4 !== 0 || sum < 4) return false;
  const target = Math.floor(sum / 4);
  matchsticks.sort((a, b) => b - a);
  const backTack = (left, right, top, bottom, i) => {
    if (left == target && right == target && top == target && bottom == target)
      return true;
    if (i > matchsticks.length - 1) {
      return false;
    }

    if (left > target || right > target || top > target || bottom > target) {
      return false;
    }

    return (
      backTack(left + matchsticks[i], right, top, bottom, i + 1) ||
      backTack(left, right + matchsticks[i], top, bottom, i + 1) ||
      backTack(left, right, top + matchsticks[i], bottom, i + 1) ||
      backTack(left, right, top, bottom + matchsticks[i], i + 1)
    );
  };
  return backTack(0, 0, 0, 0, 0);
};

console.log(makesquare([1, 1, 2, 2, 2]));
console.log(makesquare([3, 3, 3, 3, 4]));
console.log(makesquare([1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]));
