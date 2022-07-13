`There is a row of m houses in a small city, each house must be painted with one of the n colors (labeled from 1 to n), some houses that have been painted last summer should not be painted again.

A neighborhood is a maximal group of continuous houses that are painted with the same color.

For example: houses = [1,2,2,3,3,2,1,1] contains 5 neighborhoods [{1}, {2,2}, {3,3}, {2}, {1,1}].
Given an array houses, an m x n matrix cost and an integer target where:

houses[i]: is the color of the house i, and 0 if the house is not painted yet.
cost[i][j]: is the cost of paint the house i with the color j + 1.
Return the minimum cost of painting all the remaining houses in such a way that there are exactly target neighborhoods. If it is not possible, return -1.

 

Example 1:

Input: houses = [0,0,0,0,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 9
Explanation: Paint houses of this way [1,2,2,1,1]
This array contains target = 3 neighborhoods, [{1}, {2,2}, {1,1}].
Cost of paint all houses (1 + 1 + 1 + 1 + 5) = 9.
Example 2:

Input: houses = [0,2,1,2,0], cost = [[1,10],[10,1],[10,1],[1,10],[5,1]], m = 5, n = 2, target = 3
Output: 11
Explanation: Some houses are already painted, Paint the houses of this way [2,2,1,2,2]
This array contains target = 3 neighborhoods, [{2,2}, {1}, {2,2}]. 
Cost of paint the first and last house (10 + 1) = 11.
Example 3:

Input: houses = [3,1,2,3], cost = [[1,1,1],[1,1,1],[1,1,1],[1,1,1]], m = 4, n = 3, target = 3
Output: -1
Explanation: Houses are already painted with a total of 4 neighborhoods [{3},{1},{2},{3}] different of target = 3.
 

Constraints:

m == houses.length == cost.length
n == cost[i].length
1 <= m <= 100
1 <= n <= 20
1 <= target <= m
0 <= houses[i] <= n
1 <= cost[i][j] <= 104`;

const minCost = (houses, cost, m, n, target) => {
  const cache = {}; //! to memoize


  const backtrack = (prevColor, house, numNeighborhoods) => {
    if (numNeighborhoods > target) return Infinity;

    // if we have painted all the houses  return 0 if we have the correct number of neighborhoods
    if (house === m) {
      return numNeighborhoods === target ? 0 : Infinity;
      // otherwise return maximum value
    }

    // if we have already seen this combination from the cache, return the result
    const key = [prevColor, house, numNeighborhoods].join("-");
    if (cache.hasOwnProperty(key)) return cache[key];

    //  if house is already painted
    if (houses[house]) {
      // see if we have a new neighborhood
      const additionalNeighborhoods = houses[house] !== prevColor ? 1 : 0;
      return (cache[key] = backtrack(
        houses[house],
        house + 1,
        numNeighborhoods + additionalNeighborhoods
      ));
    }

    let min = Infinity;
    for (let color = 0; color < n; color++) {
      // paint the house this color by 1
      houses[house] = color + 1;
      // see if we have a new neighborhood
      const additionalNeighborhoods = houses[house] !== prevColor ? 1 : 0;
      // find the minimum price to paint all other houses with this combination
      const res = backtrack(
        houses[house],
        house + 1,
        numNeighborhoods + additionalNeighborhoods
      );
      // price to pain the house this color
      const price = cost[house][color];
      min = Math.min(min, price + res);
      // remove the paint
      houses[house] = 0;
    }
    return (cache[key] = min);
  };

  // if the result is max value, return -1;
  const result = backtrack(-1, 0, 0);
  return result === Infinity ? -1 : result;






       
  
};
