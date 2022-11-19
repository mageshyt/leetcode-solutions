`You are given an array trees where trees[i] = [xi, yi] represents the location of a tree in the garden.

You are asked to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed.

Return the coordinates of trees that are exactly located on the fence perimeter.

 

Example 1:


Input: points = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]
Output: [[1,1],[2,0],[3,3],[2,4],[4,2]]
Example 2:


Input: points = [[1,2],[2,2],[4,2]]
Output: [[4,2],[2,2],[1,2]]
`;

const tree = [
  [1, 1],
  [2, 2],
  [2, 0],
  [2, 4],
  [3, 3],
  [4, 2],
];

const outerTrees = (trees: number[][]) => {
  trees.sort((a, b) => (a[0] - b[0] == 0 ? a[1] - b[1] : a[0] - b[0])); // sort by x, then y
  const slopes = ([x1, y1], [x2, y2], [x3, y3]) =>
    (y3 - y1) * (x2 - x1) - (y2 - y1) * (x3 - x1);
  const higher = []; // upper hull
  const lower = []; // lower hull

  for (let point of trees) {
    while (
      higher.length > 1 &&
      slopes(higher[higher.length - 2], higher[higher.length - 1], point) > 0
    )
      higher.pop();
    while (
      lower.length > 1 &&
      slopes(lower[lower.length - 2], lower[lower.length - 1], point) < 0
    )
      lower.pop();

    higher.push(point);
    lower.push(point);
  }

  return [...new Set([...higher, ...lower])]; // remove duplicates
};

console.log(outerTrees(tree));
