`Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23`;

const minEatingSpeed = (piles, h) => {
  let left = 1; // ! minimum pointer
  let right = Math.max(...piles); // ! this is the max number of bananas in the array
  while (left <= right) {
    let mid = left + Math.floor((right - left) / 2);
    // !find the mid value
    // if koko can eat, mid bananas per hour in less then or equals to h time

    if (can_Bananas_Eaten(piles, h, mid)) {
      right = mid - 1;
      // we decrease the right pointer to find the best solution
    } else {
      left = mid + 1;
      // if not true, increment left pointer
    }
  }
  return left;
};
// ! this function is used to check if we can eat the bananas in the given time or not
const can_Bananas_Eaten = (piles, h, mid) => {
  let hours = 0;
  for (let banana of piles) {
    hours += Math.floor(banana / mid);
    if (banana % mid !== 0) {
      hours++;
    }
  }
  return hours <= h;
};

const piles = [3, 6, 7, 11];
const h = 8;
console.log(minEatingSpeed(piles, h));
