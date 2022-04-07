`Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.`;

const merge = (intervals) => {
  intervals.sort((a, b) => a[0] - b[0]);

  let res = [intervals[0]];
  for (let [start, end] of intervals.slice(1)) {
    const recentInterval = res[res.length - 1][1];
    if (start <= recentInterval) {
      res[res.length - 1][1] = Math.max(end, recentInterval);
    } else {
      res.push([start, end]);
    }
  }
  return res;
};
console.log(
  merge([
    [1, 3],
    [2, 6],
    [8, 10],
    [15, 18],
  ])
);
