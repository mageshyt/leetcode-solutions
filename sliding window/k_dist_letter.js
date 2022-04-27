const k_dist_letter = (string, k) => {
  const map = new Map();
  let windowStart = 0;
  let maxLength = 0;
  for (let windowEnd = 0; windowEnd < string.length; windowEnd++) {
    const rightChar = string[windowEnd];
    //! if the char no seen in map then add to the map
    if (!map.has(rightChar)) {
      map.set(rightChar, 0);
    }
    map.set(rightChar, map.get(rightChar) + 1);
    //! while loop only run when the map size is greater than k
    while (map.size > k) {
      const startChar = string[windowStart];
      //! remove the char from the map
      map.set(startChar, map.get(startChar) - 1);
      if (map.get(startChar) === 0) {
        map.delete(startChar);
      }
      windowStart++;
    }
    maxLength = Math.max(maxLength, windowEnd - windowStart + 1); //! update the maxLength
  }
  return maxLength;
};
console.log(k_dist_letter("acccpbbebi", 3)); //6

console.log(k_dist_letter("acccpbbebi", 2)); //5
