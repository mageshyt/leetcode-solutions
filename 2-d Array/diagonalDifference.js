const diagonalDifference = (nums) => {
  let left_sum = 0;
  let right_sum = 0;

  for (let i = 0; i < nums.length; i++) {
    left_sum += nums[i][i];
    right_sum += nums[i][nums.length - 1 - i];
  }
  return Math.abs(left_sum - right_sum);
};
