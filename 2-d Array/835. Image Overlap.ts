`You are given two images, img1 and img2, represented as binary, square matrices of size n x n. A binary matrix has only 0s and 1s as values.

We translate one image however we choose by sliding all the 1 bits left, right, up, and/or down any number of units. We then place it on top of the other image. We can then calculate the overlap by counting the number of positions that have a 1 in both images.

Note also that a translation does not include any kind of rotation. Any 1 bits that are translated outside of the matrix borders are erased.

Return the largest possible overlap.

 

Example 1:


Input: img1 = [[1,1,0],[0,1,0],[0,1,0]], img2 = [[0,0,0],[0,1,1],[0,0,1]]
Output: 3
Explanation: We translate img1 to right by 1 unit and down by 1 unit.

The number of positions that have a 1 in both images is 3 (shown in red).

Example 2:

Input: img1 = [[1]], img2 = [[1]]
Output: 1
Example 3:

Input: img1 = [[0]], img2 = [[0]]
Output: 0
`;

const largestOverlap = (img1: number[][], img2: number[][]): number => {
  let max = 0;
  for (let row = -img1.length + 1; row < img1.length; row++) {
    const new_nums = new Map();
    for (let col = -img1.length + 1; col < img1.length; col++) {
      max = Math.max(max, countOnes(img1, img2, row, col));
    }
  }
  return max;
};

const countOnes = (
  img1: number[][],
  img2: number[][],
  x: number,
  y: number
): number => {
  let count = 0;
  for (let row = 0; row < img1.length; row++) {
    for (let col = 0; col < img1.length; col++) {
      // case 1 if row + x is negative or col + y is negative then we are out of bounds and we can't count it so we skip
      if (row + x < 0 || col + y < 0) continue;
      // case 2 if row + x is greater than the length of the array then we are out of bounds and we can't count it so we skip
      if (row + x >= img1.length || col + y >= img1.length) continue;

      // case 3 if both are 1 then we count it
      if (img1[row][col] === 1 && img2[row + x][col + y] === 1) count++;
    }
  }
  return count;
};

const img1 = [
  [1, 1, 0],
  [0, 1, 0],
  [0, 1, 0],
];
const img2 = [
  [0, 0, 0],
  [0, 1, 1],
  [0, 0, 1],
];

console.log(largestOverlap(img1, img2));
