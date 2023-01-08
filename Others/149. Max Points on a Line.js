`Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
`;

const maxPoints = (points) => {
  if (points.length < 2) return points.length;
  let max = 2;

  for (let i = 0; i < points.length; i++) {
    for (let j = i + 1; j < points.length; j++) {
      let total = 2; //! because we already took 2 point

      for (let k = 0; k < points.length; k++) {
        if (k === i || k === j) continue;
        `
        (y2-y1)/(x2-x1) = (y3-y1)/(x3-x1)
        => (y2-y1)*(x3-x1) == (y3-y1)*(x2-x1)  therefore it is a straight line
        `;
        if (
          (points[j][1] - points[i][1]) * (points[i][0] - points[k][0]) ===
          (points[i][1] - points[k][1]) * (points[j][0] - points[i][0])
        ) {
          total++;
        }
      }
      max = Math.max(max, total);
    }
  }

  return max;
};

console.log(
  maxPoints([
    [1, 1],
    [3, 2],
    [5, 3],
    [4, 1],
    [2, 3],
    [1, 4],
  ])
);

// solution 2

const return_slope = (x1, y1, x2, y2) => {
  if (x1 - x2 === 0) return "inf";
  else return (y1 - y2) / (x1 - x2);
};

const maxPoints2 = (points) => {
  // base case
  if (points.length < 2) return points.length;

  let max = 1;
  for (let i = 0; i < points.length - max - 1; i++) {
    const map = new Map();
    for (let j = i + 1; j < points.length; j++) {
      let [x1, y1] = points[i];
      let [x2, y2] = points[j];

      let slope = return_slope(x1, y1, x2, y2);
      map.set(slope, (map.get(slope) || 0) + 1);
      max = Math.max(max, map.get(slope));
    }
  }
  return max + 1;
};

console.log(
  "👉 ",
  maxPoints2([
    [1, 1],
    [3, 2],
    [5, 3],
    [4, 1],
    [2, 3],
    [1, 4],
  ])
);
