const checkSubarraySum = (nums, k) => {
  const map = new Map();
  map.set(0, -1);
  let sum = 0;

  for (let i = 0; i < nums.length; i++) {
    sum += nums[i];
    console.log({ sum, map });
    if (k !== 0) {
      sum %= k;
    }
    if (map.has(sum)) {
      return true;
    }
    map.set(sum, i);
  }
  return false;
};

console.log(checkSubarraySum([23, 2, 4, 6, 7], 6));
