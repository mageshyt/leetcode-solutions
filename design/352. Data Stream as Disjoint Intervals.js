`Given a data stream input of non-negative integers a1, a2, ..., an, summarize the numbers seen so far as a list of disjoint intervals.

Implement the SummaryRanges class:

SummaryRanges() Initializes the object with an empty stream.
void addNum(int value) Adds the integer value to the stream.
int[][] getIntervals() Returns a summary of the integers in the stream currently as a list of disjoint intervals [starti, endi]. The answer should be sorted by starti.
 

Example 1:

Input
["SummaryRanges", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals", "addNum", "getIntervals"]
[[], [1], [], [3], [], [7], [], [2], [], [6], []]
Output
[null, null, [[1, 1]], null, [[1, 1], [3, 3]], null, [[1, 1], [3, 3], [7, 7]], null, [[1, 3], [7, 7]], null, [[1, 3], [6, 7]]]

Explanation
SummaryRanges summaryRanges = new SummaryRanges();
summaryRanges.addNum(1);      // arr = [1]
summaryRanges.getIntervals(); // return [[1, 1]]
summaryRanges.addNum(3);      // arr = [1, 3]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7);      // arr = [1, 3, 7]
summaryRanges.getIntervals(); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2);      // arr = [1, 2, 3, 7]
summaryRanges.getIntervals(); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6);      // arr = [1, 2, 3, 6, 7]
summaryRanges.getIntervals(); // return [[1, 3], [6, 7]]`;

class SummaryRanges {
  constructor() {
    this.map = new Map();
  }

  addNum(value) {
    this.map.set(value, true);
  }

  getIntervals() {
    const res = [];

    // sort the map
    const sortedMap = new Map(
      [...this.map.entries()].sort((a, b) => a[0] - b[0])
    );

    console.log('👉 sortedMap', sortedMap, '👈');
    
    for (let [key, value] of sortedMap) {
      if (res.length && res[res.length - 1][1] + 1 === key) {
        // if the current key is the next number of the last interval
        res[res.length - 1][1] = key; // update the last interval
      } else {
        // brand new interval
        res.push([key, key]);
      }
    }
    return res;
  }
}

const summaryRanges = new SummaryRanges();
summaryRanges.addNum(1); // arr = [1]
console.log(summaryRanges.getIntervals()); // return [[1, 1]]
summaryRanges.addNum(3); // arr = [1, 3]
console.log(summaryRanges.getIntervals()); // return [[1, 1], [3, 3]]
summaryRanges.addNum(7); // arr = [1, 3, 7]
console.log(summaryRanges.getIntervals()); // return [[1, 1], [3, 3], [7, 7]]
summaryRanges.addNum(2); // arr = [1, 2, 3, 7]
console.log(summaryRanges.getIntervals()); // return [[1, 3], [7, 7]]
summaryRanges.addNum(6); // arr = [1, 2, 3, 6, 7]
