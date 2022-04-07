`Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

 

Example 1:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["Piatti","The Grill at Torrey Pines","Hungry Hunter Steakhouse","Shogun"]
Output: ["Shogun"]
Explanation: The only restaurant they both like is "Shogun".
Example 2:

Input: list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KFC","Shogun","Burger King"]
Output: ["Shogun"]
Explanation: The restaurant they both like and have the least index sum is "Shogun" with index sum 1 (0+1).
`;
const findRestaurant = (list1, list2) => {
  const hash = new Map(); //
  const match = new Map(); // for our match hash
  let minIdx = Infinity;
  for (let i = 0; i < list1.length; i++) {
    hash.set(list1[i], i);
  }
  const res = [];
  for (let i = 0; i < list2.length; i++) {
    const currRes = list2[i];
    if (hash.has(currRes)) {
      const idxSum = i + hash.get(currRes);
      minIdx = Math.min(minIdx, idxSum);
      match.set(currRes, idxSum); //! going to set current restaurant to the index sum
    }
  }
  for (let [key, value] of match) {
    //! we will check if the value is equal to the minIdx
    if (value === minIdx) res.push(key);
  }

  return res;
};
(list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]),
  (list2 = ["KFC", "Burger King", "Tapioca Express", "Shogun"]);
console.log(findRestaurant(list1, list2));
