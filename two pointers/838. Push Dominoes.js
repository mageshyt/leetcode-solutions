`There are n dominoes in a line, and we place each domino vertically upright. In the beginning, we simultaneously push some of the dominoes either to the left or to the right.

After each second, each domino that is falling to the left pushes the adjacent domino on the left. Similarly, the dominoes falling to the right push their adjacent dominoes standing on the right.

When a vertical domino has dominoes falling on it from both sides, it stays still due to the balance of the forces.

For the purposes of this question, we will consider that a falling domino expends no additional force to a falling or already fallen domino.

You are given a string dominoes representing the initial state where:

dominoes[i] = 'L', if the ith domino has been pushed to the left,
dominoes[i] = 'R', if the ith domino has been pushed to the right, and
dominoes[i] = '.', if the ith domino has not been pushed.
Return a string representing the final state.

 

Example 1:

Input: dominoes = "RR.L"
Output: "RR.L"
Explanation: The first domino expends no additional force on the second domino.
Example 2:


Input: dominoes = ".L.R...LR..L.."
Output: "LL.RR.LLRRLL.."
 

Constraints:

n == dominoes.length
1 <= n <= 105
dominoes[i] is either 'L', 'R', or '.'.`;

const pushDominoes = (dominoes) => {
  let left = 0;
  const len = dominoes.length;

  for (let right = 0; right < len; right++) {
    //! ignore case
    if (dominoes[right] === ".") continue;
    else if (dominoes[left] === "L" && dominoes[right] === "R") {
    }
    //! case 1: both are equal
    else if (
      dominoes[left] === dominoes[right] ||
      (dominoes[left] === "." && dominoes[right] === "L")
    ) {
      for (let i = left; i < right; i++) dominoes[i] = dominoes[right];
    }

    // case 2: left is R and right is L
    else if (dominoes[left] === "R" && dominoes[right] === "L") {
      const m_dots = Math.floor((right - left - 1) / 2);
      console.log("m_dots", m_dots);
      for (let k = 1; k <= m_dots; k++) {
        dominoes[right - k] = "L";
        dominoes[left + k] = "R";
      }
    }
    // update left
    left = right;
  }

  // case 3: left is R and right is .
  if (dominoes[left] === "R") {
    for (let i = left; i < len; i++) dominoes[i] = "R";
  }
  return dominoes;
};

console.log(pushDominoes("RR.L"));

console.log(pushDominoes(".L.R...LR..L.."));
