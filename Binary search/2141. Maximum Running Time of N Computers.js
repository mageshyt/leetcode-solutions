`You have n computers. You are given the integer n and a 0-indexed integer array batteries where the ith battery can run a computer for batteries[i] minutes. You are interested in running all n computers simultaneously using the given batteries.

Initially, you can insert at most one battery into each computer. After that and at any integer time moment, you can remove a battery from a computer and insert another battery any number of times. The inserted battery can be a totally new battery or a battery from another computer. You may assume that the removing and inserting processes take no time.

Note that the batteries cannot be recharged.

Return the maximum number of minutes you can run all the n computers simultaneously.

 

Example 1:


Input: n = 2, batteries = [3,3,3]
Output: 4
Explanation: 
Initially, insert battery 0 into the first computer and battery 1 into the second computer.
After two minutes, remove battery 1 from the second computer and insert battery 2 instead. Note that battery 1 can still run for one minute.
At the end of the third minute, battery 0 is drained, and you need to remove it from the first computer and insert battery 1 instead.
By the end of the fourth minute, battery 1 is also drained, and the first computer is no longer running.
We can run the two computers simultaneously for at most 4 minutes, so we return 4.
`;

// Function to check if it is possible to run the computer for a given time using the batteries
const isPossible = (batteries, time, computer) => {
  let total_time = 0;

  // Loop through all the batteries
  for (let Btime of batteries) {
    // If the battery runtime is less than the required time, use the entire battery
    if (Btime < time) total_time += Btime;
    else total_time += time;
  }

  // Check if the total time accumulated from batteries is greater than or equal to the required time for the computer
  return total_time >= time * computer;
};

// Function to find the maximum runtime that can be achieved with given batteries for 'n' computers
const maxRunTime = (n, batteries) => {
  let low = 0;
  let high = batteries.reduce((a, b) => a + b, 0);

  const size = batteries.length;

  let ans = 0;

  // Binary search loop to find the maximum runtime
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);

    if (isPossible(batteries, mid, n)) {
      // If it is possible to run 'n' computers for 'mid' time, update the answer and search for larger runtimes
      ans = mid;
      low = mid + 1;
    } else {
      // If it is not possible, search for smaller runtimes
      high = mid - 1;
    }
  }
  return ans; // Return the maximum runtime that can be achieved with the given batteries
};

const n = 2;
console.log(maxRunTime(n, [3, 3, 3]));
