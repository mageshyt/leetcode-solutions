`You are given m arrays, where each array is sorted in ascending order.

You can pick up two integers from two different arrays (each array picks one) and 
calculate the distance. We define the distance between two integers a and b to be their absolute difference |a - b|.

Return the maximum distance.

 

Example 1:

Input: arrays = [[1,2,3],[4,5],[1,2,3]]
Output: 4
Explanation: One way to reach the maximum distance 4 is to pick 1 in the first or third array and pick 5 in the second array.
Example 2:

Input: arrays = [[1],[1]]
Output: 0`;

const maxDistance = (array) => {
  let min = array[0][0];
  let max = array[0][array[0].length - 1];
  let result = 0;

  for (let i = 1; i < array.length; i++) {
    const currentMin = array[i][0];
    const currentMax = array[i][array[i].length - 1];
    result = Math.max(
      result,
      Math.abs(currentMax - min),
      Math.abs(max - currentMin)
    );
    min = Math.min(min, currentMin);
    max = Math.max(max, currentMax);
  }

  return result;
};

// Time Complexity: O(n)
// Space Complexity: O(1)

// Test Cases
console.log(
  maxDistance([
    [1, 4],
    [0, 5],
  ])
); // 4
