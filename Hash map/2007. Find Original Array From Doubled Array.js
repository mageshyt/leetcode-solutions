`An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, and then randomly shuffling the resulting array.

Given an array changed, return original if changed is a doubled array. If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.

 

Example 1:

Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
- Twice the value of 1 is 1 * 2 = 2.
- Twice the value of 3 is 3 * 2 = 6.
- Twice the value of 4 is 4 * 2 = 8.
Other original arrays could be [4,3,1] or [3,1,4].
Example 2:

Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.
Example 3:

Input: changed = [1]
Output: []
Explanation: changed is not a doubled array.`;

const findOriginalArray = (changed) => {
  const len = changed.length;
  if (len % 2 !== 0) return []; //! if the length of the array is odd, return empty array
  const map = new Map(); //! create a map to store the values
  const res = [];
  changed.sort((a, b) => a - b); //! sort the array
  for (let num of changed) {
    map.set(num, (map.get(num) || 0) + 1); //! store the values in the map
  }
  for (let num of changed) {
    if (map.get(num) === 0) continue; //! if the value is 0, skip it
    if (map.get(num * 2) === 0) return []; //! if the value is 0, return empty array
    res.push(num); //! push the value to the result array
    map.set(num, map.get(num) - 1); //! decrement the value by 1
    map.set(num * 2, map.get(num * 2) - 1); //! decrement the value by 1
  }
  return res.length === len / 2 ? res : []; //! if the length of the result array is half of the length of the changed array, return the result array, else return empty array
};
console.log(findOriginalArray([1, 3, 4, 2, 6, 8]));
console.log(findOriginalArray([6, 3, 0, 1]));
