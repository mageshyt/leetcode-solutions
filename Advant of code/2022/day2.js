`Appreciativefof your help yesterday, one Elf gives you an encrypted strategy guide (your puzzle input) that they say will be sure to help you win. "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. The second column--" Suddenly, the Elf is called away to help with someone's tent.

The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. Winning every time would be suspicious, so the responses must have been carefully chosen.

The winner of the whole tournament is the player with the highest score. Your total score is the sum of your scores for each round. The score for a single round is the score for the shape you selected (1 for Rock, 2 for Paper, and 3 for Scissors) plus the score for the outcome of the round (0 if you lost, 3 if the round was a draw, and 6 if you won).

Since you can't be sure if the Elf is trying to help you or trick you, you should calculate the score you would get if you were to follow the strategy guide.

For example, suppose you were given the following strategy guide:

A Y
B X
C Z
This strategy guide predicts and recommends the following:

In the first round, your opponent will choose Rock (A), and you should choose Paper (Y). This ends in a win for you with a score of 8 (2 because you chose Paper + 6 because you won).
In the second round, your opponent will choose Paper (B), and you should choose Rock (X). This ends in a loss for you with a score of 1 (1 + 0).
The third round is a draw with both players choosing Scissors, giving you a score of 3 + 3 = 6.
In this example, if you were to follow the strategy guide, you would get a total score of 15 (8 + 1 + 6).`;

// read the file from testcase.txt
const fs = require("fs");
const path = require("path");
const input = fs.readFileSync(path.join(__dirname, "testcase.txt"), "utf8");
// split the input into array
const inputArray = input.split("\n");

const rockPaperScissors = (array) => {
  const values = {
    A: 1,
    B: 2,
    C: 3,
    X: 1,
    Y: 2,
    Z: 3,
  };
  let score = 0;

  for (let i of array) {
    const [opponent, you] = i.split(" ");
    // if both are same then add 3 to score and value of opponent
    if (values[opponent] === values[you]) {
      score += 3 + values[opponent];
    }
    // if opponent score is greater than you then add 0 to score and value of you
    if (values[opponent] > values[you]) {
      score += 0 + values[you];
    }
    // if opponent score is less than you then add 6 to score and value of opponent
    if (values[opponent] < values[you]) {
      score += 6 + values[you];
    }
  }

  return score;
};
console.log(rockPaperScissors(inputArray));
