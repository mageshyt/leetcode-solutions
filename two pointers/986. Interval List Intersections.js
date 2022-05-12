`You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

Return the intersection of these two interval lists.

A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 

Example 1:


Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
Example 2:

Input: firstList = [[1,3],[5,9]], secondList = []
Output: []
 `;

const intervalIntersection = (firstList, secondList) => {
  const ans = [];
  let left = 0;
  let right = 0;
  while (left < firstList.length && right < secondList.length) {
    const [start, end] = firstList[left];
    const [start2, end2] = secondList[right];

    const low = Math.max(start, start2); // start of the intersection
    const high = Math.min(end, end2); // end of the intersection

    if (low <= high) { 
      ans.push([low, high]);
    }
    //! we will remove the smallest interval
    if (end < end2) {
      console.log({ 1: firstList[left], 2: secondList[right], low, high });
      left++;
    } else {
      console.log({ 2: secondList[right], 1: firstList[left], low, high });
      right++;
    }
  }
  return ans;
};

console.log(
  intervalIntersection(
    [
      [0, 2],
      [5, 10],
      [13, 23],
      [24, 25],
    ],
    [
      [1, 5],
      [8, 12],
      [15, 24],
      [25, 26],
    ]
  )
);
