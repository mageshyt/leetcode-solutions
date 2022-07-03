`You are given a rectangular cake of size h x w and two arrays of integers horizontalCuts and verticalCuts where:

horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly, and
verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.
Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays horizontalCuts and verticalCuts. Since the answer can be a large number, return this modulo 109 + 7.

 

Example 1:


Input: h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3]
Output: 4 
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green piece of cake has the maximum area.
Example 2:


Input: h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1]
Output: 6
Explanation: The figure above represents the given rectangular cake. Red lines are the horizontal and vertical cuts. After you cut the cake, the green and yellow pieces of cake have the maximum area.
Example 3:

Input: h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3]
Output: 9`;

const maxArea = (h, w, horizontalCuts, verticalCuts) => {
  horizontalCuts = [0, ...horizontalCuts.sort((a, b) => a - b), h];
  verticalCuts = [0, ...verticalCuts.sort((a, b) => a - b), w];

  let maxHeight = Number.MIN_SAFE_INTEGER;
  let maxWidth = Number.MIN_SAFE_INTEGER;
  for (let i = 1; i < horizontalCuts.length; i++) {
    // ! find the max distance between horizontal cuts
    maxHeight = Math.max(maxHeight, horizontalCuts[i] - horizontalCuts[i - 1]);
  }
  for (let i = 1; i < verticalCuts.length; i++) {
    // ! find the max difference between two cuts
    maxWidth = Math.max(maxWidth, verticalCuts[i] - verticalCuts[i - 1]);
  }
  return (BigInt(maxHeight) * BigInt(maxWidth)) % BigInt(Math.pow(10, 9) + 7);
};

console.log(maxArea(1000000000, 1000000000, [2], [2]));
