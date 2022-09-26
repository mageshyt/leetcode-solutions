`Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).

 

Example 1:

Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]

Example 2:

Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
`;

const equalPairs = (grid) => {
  const map = new Map();

  const rows = grid.length;

  const cols = grid[0].length;

  for (let r = 0; r < rows; r++) {
    let seq = "";
    let seq2 = "";
    for (let c = 0; c < cols; c++) {
      seq += grid[r][c];
      seq2 += grid[c][r];
    }
    map.set(seq, map.get(seq) + 1 || 1);
    map.set(seq2, map.get(seq2) + 1 || 1);
  }

  let count = 0;
  for (let [key, value] of map.entries()) {
    if (value > 1) {
      console.log(key, value);
      count += 1;
    }
  }
  return count;
};
console.log(
  equalPairs([
    [3, 2, 1],
    [1, 7, 6],
    [2, 7, 7],
  ])
);
grid = [
  [3, 1, 2, 2],
  [1, 4, 4, 5],
  [2, 4, 2, 2],
  [2, 4, 2, 2],
];
console.log(equalPairs(grid));
