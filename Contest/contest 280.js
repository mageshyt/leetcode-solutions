`6004. Count Operations to Obtain Zero

You are given two non-negative integers num1 and num2.

In one operation, if num1 >= num2, you must subtract num2 from num1, otherwise subtract num1 from num2.

For example, if num1 = 5 and num2 = 4, subtract num2 from num1, thus obtaining num1 = 1 and num2 = 4. However, if num1 = 4 and num2 = 5, after one operation, num1 = 4 and num2 = 1.
Return the number of operations required to make either num1 = 0 or num2 = 0.


Example 1:

Input: num1 = 2, num2 = 3
Output: 3
Explanation: 
- Operation 1: num1 = 2, num2 = 3. Since num1 < num2, we subtract num1 from num2 and get num1 = 2, num2 = 3 - 2 = 1.
- Operation 2: num1 = 2, num2 = 1. Since num1 > num2, we subtract num2 from num1.
- Operation 3: num1 = 1, num2 = 1. Since num1 == num2, we subtract num2 from num1.
Now num1 = 0 and num2 = 1. Since num1 == 0, we do not need to perform any further operations.
So the total number of operations required is 3.
Example 2:

Input: num1 = 10, num2 = 10
Output: 1
Explanation: 
- Operation 1: num1 = 10, num2 = 10. Since num1 == num2, we subtract num2 from num1 and get num1 = 10 - 10 = 0.
Now num1 = 0 and num2 = 10. Since num1 == 0, we are done.
So the total number of operations required is 1.

`;

const countOperations = (num1, num2) => {
  let count = 0;
  while (num1 !== 0 && num2 !== 0) {
    if (num1 >= num2) {
      num1 -= num2;
      count++;
    } else {
      num2 -= num1;
      count++;
    }
  }
  return count;
};
// console.log(countOperations(2, 3));

`You are given an array of positive integers beans, where each integer represents the number of magic beans found in a particular magic bag.

Remove any number of beans (possibly none) from each bag such that the number of beans in each remaining non-empty bag (still containing at least one bean) is equal. Once a bean has been removed from a bag, you are not allowed to return it to any of the bags.

Return the minimum number of magic beans that you have to remove.

 

Example 1:

Input: beans = [4,1,6,5]
Output: 4
Explanation: 
- We remove 1 bean from the bag with only 1 bean.
  This results in the remaining bags: [4,0,6,5]
- Then we remove 2 beans from the bag with 6 beans.
  This results in the remaining bags: [4,0,4,5]
- Then we remove 1 bean from the bag with 5 beans.
  This results in the remaining bags: [4,0,4,4]
We removed a total of 1 + 2 + 1 = 4 beans to make the remaining non-empty bags have an equal number of beans.
There are no other solutions that remove 4 beans or fewer.
`;

const minimumRemoval = (beans) => {
  let count = 0;
  let min_number = Math.min(...beans);
  beans[beans.indexOf(min_number)] = 0;
  console.log(beans);
  beans.sort((a, b) => a - b);
  beans.forEach((bean) => {
    beans[beans.indexOf(bean)] = -bean;
    count += bean;
  });
  console.log(beans);
  return count;
};
// console.log(minimumRemoval([2, 10, 3, 2]));

`You are given a 0-indexed array nums consisting of n positive integers.

The array nums is called alternating if:

nums[i - 2] == nums[i], where 2 <= i <= n - 1.
nums[i - 1] != nums[i], where 1 <= i <= n - 1.
In one operation, you can choose an index i and change nums[i] into any positive integer.

Return the minimum number of operations required to make the array alternating.

 

Example 1:

Input: nums = [3,1,3,2,4,3]
Output: 3
Explanation:
One way to make the array alternating is by converting it to [3,1,3,1,3,1].
The number of operations required in this case is 3.
It can be proven that it is not possible to make the array alternating in less than 3 operations. 
Example 2:

Input: nums = [1,2,2,2,2]
Output: 2
Explanation:
One way to make the array alternating is by converting it to [1,2,1,2,1].
The number of operations required in this case is 2.
Note that the array cannot be converted to [2,2,2,2,2] because in this case nums[0] == nums[1] which violates the conditions of an alternating array.`;

const minimumOperations = (nums) => {
  let left = 0;
  let right = 1;
  let num = 0;
  let nums_length = nums.length;
  for (let i = 0; i < nums_length; i++) {
    const current = nums[i];
    const next = nums[i + 1];
    if (nums[i + 2] !== current && i + 2 < nums_length) {
      nums[i + 2] = nums[i];
      num++;
    }
    if (nums[i + 3] !== next && i + 3 < nums_length) {
      nums[i + 3] = nums[i + 1];
      num++;
    }
  }
  //   for (let i = 1; i < nums_length; i++) {
  //     const current = nums[i];
  //     if (nums[i + 2] !== current) {
  //       nums[i + 2] = nums[i];
  //       num++;
  //     }
  //   }
  console.log(nums);
  return num;
};
console.log(minimumOperations([1,2,2,2,2]));
