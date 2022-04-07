`
Given an array of distinct integers arr, find all pairs of elements with the minimum absolute difference of any two elements. 

Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows

a, b are from arr
a < b
b - a equals to the minimum absolute difference of any two elements in arr
 

Example 1:

Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
`;
const minimumAbsoluteDifference = (arr) => {
  const sorted = arr.sort((a, b) => a - b);
  let res = Infinity;
  const ans = [];
  for (let i = 0; i < sorted.length - 1; i++) {
    const value = sorted[i + 1] - sorted[i];
    res = Math.min(res, value);
  }
  for (let i = 0; i < sorted.length; i++) {
    if (sorted[i + 1] - sorted[i] === res) {
      ans.push([sorted[i], sorted[i + 1]]);
    }
  }
  return ans;
  //   return res;
};

const result = minimumAbsoluteDifference(arr);
console.log(result);
