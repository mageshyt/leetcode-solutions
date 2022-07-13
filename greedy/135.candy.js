`There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.

 

Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
Constraints:

    n == ratings.length
    1 <= n <= 2 * 104
    0 <= ratings[i] <= 2 * 104

`;

const candy = (ratings) => {
  const result = new Array(ratings.length).fill(1);
  for (let i = 1; i < ratings.length; i++) {
    if (ratings[i] > ratings[i - 1]) {
      result[i] = result[i - 1] + 1;
    }
  }
  let sum = result[ratings.length - 1];
  for (let i = ratings.length - 2; i >= 0; i--) {
    const current = ratings[i];
    const next = ratings[i + 1];
    if (current > next) {
      result[i] = Math.max(result[i], result[i + 1] + 1);
    }
    sum += result[i];
  }
  return sum;
};

console.log(candy([1, 0, 2]));
console.log(candy([3, 5, 2, 1]));
console.log(candy([4, 6, 7, 0, 2]));    
console.log(candy([1, 2, 87, 87, 87, 2, 1]));
