`ou are given an integer n. We reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this so that the resulting number is a power of two.

 

Example 1:

Input: n = 1
Output: true
Example 2:

Input: n = 10
Output: false
`;

const reorderedPowerOf2 = (n) => {
  const nums = Form_Freq_Arr(n);
  for (let i = 0; i < 31; i++) {
    const power = Math.pow(2, i);
    const power_nums = Form_Freq_Arr(power);
    console.log(power, power_nums);
    if (compare_arr(nums, power_nums)) return true;
  }
  return false;
};
const Form_Freq_Arr = (num) => {
  const nums = new Array(10).fill(0);
  while (num > 0) {
    nums[num % 10]++;

    num = Math.floor(num / 10);
  }
  return nums;
};

const compare_arr = (arr1, arr2) => {
  if (arr1.length !== arr2.length) return false;
  for (let i = 0; i < arr1.length; i++) {
    if (arr1[i] !== arr2[i]) return false;
  }
  return true;
};

console.log(reorderedPowerOf2(4));
