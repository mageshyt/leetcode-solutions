const largestDivisibleSubset = (nums) => {
  // Sort the nums
  nums.sort((a,b)=>a-b);
  const cache = new Map();
  const size = nums.length;
  const dfs = (i) => {
    // if already we computed i then return it
    if (i == size) {
      return [];
    }
    if (cache.has(i)) {
      return cache.get(i);
    }
    let res = [nums[i]];

    for (let j = i + 1; j <= size; j++) {
      //if both  mod are same
      if (nums[j] % nums[i] == 0) {
        temp = [nums[i], ...dfs(j)];
        if (temp.length > res.length) {
          res = temp;
        }
      }
    }
    cache[i] = res;

    return cache[i];
  };

  res = [];
  for (let index = 0; index < size; index++) {
    const temp = dfs(index);

    if (res.length < temp.length) {
      res = temp;
    }
  }
  return res;
};

console.log(largestDivisibleSubset([3, 4, 16, 8])); // [1, 2] or [1, 3]
