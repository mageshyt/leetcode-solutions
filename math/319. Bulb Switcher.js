`There are n bulbs that are initially off. You first turn on all the bulbs, then you turn off every second bulb.

On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). For the ith round, you toggle every i bulb. For the nth round, you only toggle the last bulb.

Return the number of bulbs that are on after n rounds.

 

Example 1:


Input: n = 3
Output: 1
Explanation: At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off]. 
So you should return 1 because there is only one bulb is on.`;

const bulbSwitch = (n) => {
  let bulbs = new Array(n).fill(false);

  for (let i = 1; i <= n; i++) {
    for (let j = i - 1; j < n; j += i) {
      bulbs[j] = !bulbs[j];
    }
  }

  return bulbs.filter((bulb) => bulb === true).length;
};

const bulbSwitch2 = (n) => parseInt(Math.sqrt(n));

console.log("👉 ", bulbSwitch2(3));
