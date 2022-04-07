`Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).`;

// perfect square
const IsPerfectSquare = (n) => Number.isInteger(Math.sqrt(n));

const winnerSquareGame = (n) => {
  if (IsPerfectSquare(n)) return true;
  if (n <= 0) {
    return false;
  }
  for (let j = 1; j * j < n + 1; j++) {
    if (!winnerSquareGame(n - j * j)) {
      return true;
    }
  }
  return false;
};

n = 1;
console.log(winnerSquareGame(n));

var isSquare = (n) => Number.isInteger(Math.sqrt(n));
console.log(isSquare());
