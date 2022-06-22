`Given an integer array sorted in non-decreasing order, there is exactly one integer in the array that occurs more than 25% of the time, return that integer.

 

Example 1:

Input: arr = [1,2,2,6,6,6,6,7,10]
Output: 6
Example 2:

Input: arr = [1,1]
Output: 1`;

const findSpecialInteger = (arr) => {
  if (arr.length === 1) return arr[0];
  const map = new Map();
  for (let num of arr) {
    map.set(num, map.get(num) + 1 || 1);
    const acc = (map.get(num) / arr.length) * 100;

    if (acc > 25) return num;
  }
  console.log(map);
};
console.log(findSpecialInteger([1, 2, 3, 3]));
console.log(findSpecialInteger([1, 2, 2, 6, 6, 6, 6, 7, 10]));
