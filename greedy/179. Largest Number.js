`Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"`;

const largestNumber = (nums) => {
  nums = nums.map((num) => num.toString());
  const compare = (a, b) => (a + b - (b + a) > 0 ? -1 : 1);

  nums.sort((a, b) => compare(a, b));
  return String(parseInt(nums.join("")));
};
console.log(largestNumber([10, 2]));
