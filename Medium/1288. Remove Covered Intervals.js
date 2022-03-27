`Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.`;

const removeCoveredIntervals = (intervals) => {
  intervals.sort((a, b) => a[0] - b[1]);
  intervals.sort((a, b) => a[0] - b[0]);
  console.log(intervals);
  const result = [intervals[0]];
  for (let [left, right] of intervals.slice(1)) {
    let prevLeft = result[result.length - 1][0];
    let prevRight = result[result.length - 1][1];
    if (left >= prevLeft && right <= prevRight) continue;
    result.push([left, right]);
  }
  return result.length;
};
console.log(
  removeCoveredIntervals([
    [1, 4],
    [3, 6],
    [2, 8],
  ])
);
console.log(
  removeCoveredIntervals([
    [1, 4],
    [2, 3],
  ])
);
console.log(
  removeCoveredIntervals([
    [1, 2],
    [1, 4],
    [3, 4],
  ])
);
