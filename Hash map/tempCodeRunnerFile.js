const sol = (nums) => {
  let count = 0;
  let pre_max = nums[0];
  for (let i = 1; i < nums.length; i++) {
    if (count > 1) return false;
    if (nums[i] > pre_max) {
      pre_max = nums[i];
    } else {
      count++;
      i += 1;
    }
  }
  return true;
};
sequence = [3, 6, 5, 8, 10, 20, 15];
sol(sequence);
