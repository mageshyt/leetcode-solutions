`There are n piles of coins on a table. Each pile consists of a positive number of coins of assorted denominations.

In one move, you can choose any coin on top of any pile, remove it, and add it to your wallet.

Given a list piles, where piles[i] is a list of integers denoting the composition of the ith pile from top to bottom, and a positive integer k, return the maximum total value of coins you can have in your wallet if you choose exactly k coins optimally.

 

Example 1:


Input: piles = [[1,100,3],[7,8,9]], k = 2
Output: 101
Explanation:
The above diagram shows the different ways we can choose k coins.
The maximum total we can obtain is 101.
Example 2:

Input: piles = [[100],[100],[100],[100],[100],[100],[1,1,1,1,1,1,700]], k = 7
Output: 706
Explanation:
The maximum total can be obtained if we choose all coins from the last pile.`;

interface IMaxValueOfCoins {
  piles: number[][];
  k: number;
}

const maxValueOfCoin = (piles: number[][], k: number): number => {
  const len = piles.length;

  const cache = Array.from({ length: k + 1 }, () =>
    Array.from({ length: k + 1 }, () => -1)
  );

  const dfs = (i: number, coins: number): number => {
    // base case
    if (len === i) {
      return 0;
    }

    cache[i][coins] = Math.max(cache[i][coins], -1);
    let curpile = 0;

    for (let j = 0; j < Math.min(coins, piles[i].length); j++) {
      curpile += piles[i][j];
      const temp = curpile + dfs(i + 1, coins - j - 1);

      cache[i][coins] = Math.max(cache[i][coins], temp);
    }

    return cache[i][coins];
  };

  console.log("cache", cache);
  return dfs(0, k);
};

console.log(
  "maxValueOfCoin",
  maxValueOfCoin(
    [
      [1, 100, 3],
      [7, 8, 9],
    ],
    2
  )
);


