`You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

 

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]
Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].`;

const insert = (intervals, newInterval) => {
  intervals.push(newInterval);
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
  insert(
    [
      [1, 3],
      [6, 9],
    ],
    [2, 5]
  )
);
