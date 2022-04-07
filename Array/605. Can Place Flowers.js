`You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers
cannot be planted in adjacent plots.
Given an integer array flowerbed containing o 's and 1 's, where 0 means empty and 1 means not
empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-
adjacent-flowers rule.
Example 1:
  Input: flowerbed = [1,0,0,0,1], n = 1
  Output: true
Example 2:
  Input: flowerbed = [1,0,0,0,1], n = 2
  Output: false`;

const canPlaceFlowers = (flowerbed, n) => {
  flowerbed = [0, ...flowerbed, 0];
  for (let i = 1; i < flowerbed.length; i++) {
    const curr = flowerbed[i];
    const next = flowerbed[i + 1];
    const prev = flowerbed[i - 1];
    if (curr === 0 && next === 0 && prev === 0) {
      n--;
      flowerbed[i] = 1;
    }
    if (n <= 0) return true;
  }
  //   console.log(flowerbed);
  return false;
};

(flowerbed = [0, 0, 1, 0, 1]), (n = 1);

const ans = canPlaceFlowers(flowerbed, n);
console.log(ans);
