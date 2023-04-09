`You are given a 0-indexed two-dimensional integer array nums.

Return the largest prime number that lies on at least one of the diagonals of nums. In case, no prime is present on any of the diagonals, return 0.

Note that:

An integer is prime if it is greater than 1 and has no positive integer divisors other than 1 and itself.
An integer val is on one of thediagonals of nums if there exists an integer i for which nums[i][i] = val or an i for which nums[i][nums.length - i - 1]= val.


In the above diagram, one diagonal is [1,5,9] and another diagonal is [3,5,7].

 

Example 1:

Input: nums = [[1,2,3],[5,6,7],[9,10,11]]
Output: 11
Explanation: The numbers 1, 3, 6, 9, and 11 are the only numbers present on at least one of the diagonals. Since 11 is the largest prime, we return 11.
Example 2:

Input: nums = [[1,2,3],[5,17,7],[9,11,10]]
Output: 17
Explanation: The numbers 1, 3, 9, 10, and 17 are all present on at least one of the diagonals. 17 is the largest prime, so we return 17.
`;

const diagonalPrime = (nums) => {
  // get all the diagonals

  const diagonals = [];

  for (let i = 0; i < nums.length; i++) {
    for (let j = 0; j < nums.length; j++) {
      if (i === j) diagonals.push(nums[i][j]);

      if (i + j === nums.length - 1) diagonals.push(nums[i][j]);
    }
  }

  // check if the diagonals are prime

  let maxPrime = 0;

  for (let i = 0; i < diagonals.length; i++) {
    if (IsPrime(diagonals[i])) {
      maxPrime = Math.max(maxPrime, diagonals[i]);
    }
  }

  return maxPrime;
};
const IsPrime = (num) => {
  if (num <= 1) return false;
  if (num <= 3) return true;

  if (num % 2 == 0 || num % 3 == 0) return false;

  for (let i = 5; i * i <= num; i = i + 6) {
    if (num % i == 0 || num % (i + 2) == 0) return false;
  }

  return true;
};

let nums = [
  [1, 2, 3],
  [5, 6, 7],
  [9, 10, 11],
];

// diagonalPrime(nums);

`You are given a 0-indexed integer array nums. There exists an array arr of length nums.length, where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

 

Example 1:

Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 

Example 2:

Input: nums = [0,5,3]
Output: [0,0,0]
Explanation: Since each element in nums is distinct, arr[i] = 0 for all i.`;

const distance = (nums) => {
  adj = new Map();

  for (let i = 0; i < nums.length; i++) {
    if (!adj.has(nums[i])) {
      adj.set(nums[i], new Set());
    }

    adj.get(nums[i]).add(i);
  }

  console.log(
    "👉 ~ file: 2614. Prime In Diagonal.js ~ line 100 ~ distance ~ adj",
    adj
  );

  const res = [];

  for (let i = 0; i < nums.length; i++) {
    const curr = nums[i];

    let sum = 0;

    for (let j = 0; j < nums.length; j++) {
      if (nums[j] === curr && i !== j) {
        sum += Math.abs(j - i);
      }
    }

    res.push(sum);
  }

 

  return res;
};

nums = [1, 3, 1, 1, 2];

distance(nums);
