`You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

The 1st place athlete's rank is "Gold Medal".
The 2nd place athlete's rank is "Silver Medal".
The 3rd place athlete's rank is "Bronze Medal".
For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").
Return an array answer of size n where answer[i] is the rank of the ith athlete.

 

Example 1:

Input: score = [5,4,3,2,1]
Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].
Example 2:

Input: score = [10,3,8,9,4]
Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
Explanation: The placements are [1st, 5th, 3rd, 2nd, 4th].
`;
const { MaxHeap, MinHeap } = require("datastructures-js");

const mHeap = new MinHeap();
mHeap.insert(5);
mHeap.insert(4);
mHeap.insert(3);

const findRelativeRanks = (scores) => {
  const medals = ["Gold Medal", "Silver Medal", "Bronze Medal"];
  const sortedScores = scores.slice().sort((a, b) => b - a);
  for (let i = 0; i < scores.length; i++) {
    const score = scores[i];
    if (score === sortedScores[0]) {
      scores[i] = medals[0];
    } else if (score === sortedScores[1]) {
      scores[i] = medals[1];
    } else if (score === sortedScores[2]) {
      scores[i] = medals[2];
    } else {
      scores[i] = (sortedScores.indexOf(score) + 1).toString();
    }
  }
  return scores;
};

console.log(findRelativeRanks([10, 3, 8, 9, 4]));
