const maximumCount = (nums) => {
  let po_count = 0;
  let ne_count = 0;

  for (let i = 0; i < nums.length; i++) {
    if (nums[i] > 0) {
      po_count++;
    }
    if (nums[i] < 0) {
      ne_count++;
    }
  }

  if (po_count > ne_count) {
    return po_count;
  }
  return ne_count;
};

`You are given a 0-indexed integer array nums and an integer k. You have a starting score of 0.

In one operation:

choose an index i such that 0 <= i < nums.length,
increase your score by nums[i], and
replace nums[i] with ceil(nums[i] / 3).
Return the maximum possible score you can attain after applying exactly k operations.

The ceiling function ceil(val) is the least integer greater than or equal to val.

 

Example 1:

Input: nums = [10,10,10,10,10], k = 5
Output: 50
Explanation: Apply the operation to each array element exactly once. The final score is 10 + 10 + 10 + 10 + 10 = 50.
Example 2:

Input: nums = [1,10,3,3,3], k = 3
Output: 17
Explanation: You can do the following operations:
Operation 1: Select i = 1, so nums becomes [1,4,3,3,3]. Your score increases by 10.
Operation 2: Select i = 1, so nums becomes [1,2,3,3,3]. Your score increases by 4.
Operation 3: Select i = 2, so nums becomes [1,1,1,3,3]. Your score increases by 3.
The final score is 10 + 4 + 3 = 17.
 `;

`You are given two 0-indexed strings word1 and word2.

A move consists of choosing two indices i and j such that 0 <= i < word1.length and 0 <= j < word2.length and swapping word1[i] with word2[j].

Return true if it is possible to get the number of distinct characters in word1 and word2 to be equal with exactly one move. Return false otherwise.


Example 1:

Input: word1 = "ac", word2 = "b"
Output: false
Explanation: Any pair of swaps would yield two distinct characters in the first string, and one in the second string

`;

const isItPossible = (word1, word2) => {
  let word1Arr = word1.split("");
  let word2Arr = word2.split("");

  const hash_word1 = new Map();
  const hash_word2 = new Map();

  for (let i = 0; i < word1Arr.length; i++) {
    if (hash_word1.has(word1Arr[i])) {
      // put the idx of the character in the map
      hash_word1.set(word1Arr[i], [hash_word1.get(word1Arr[i])[0] + 1, i]);
    } else {
      hash_word1.set(word1Arr[i], [1, i]);
    }
  }

  for (let i = 0; i < word2Arr.length; i++) {
    if (hash_word2.has(word2Arr[i])) {
      // put the idx of the character in the map
      hash_word2.set(word2Arr[i], [hash_word2.get(word2Arr[i])[0] + 1, i]);
    } else {
      hash_word2.set(word2Arr[i], [1, i]);
    }
  }

  // # now we have to swap the characters

  for (let [key, value] of hash_word1) {
    // find the key which is not present in word2
    if (!hash_word2.has(key)) {
      // wap the character with the character which is present in word2
      const [count, idx] = value;
      //    swap with max count character
      let max = 0;
      let idx2 = 0;
      let char = "";
      for (let [key2, value2] of hash_word2) {
        if (value2[0] > max) {
          max = value2[0];
          idx2 = value2[1];
          char = key2;
        }
      }
      // swap the character
      hash_word2.set(key, [1, idx]);

      // delete the character from hash_word2 is it is 1
      if (hash_word2.get(char)[0] === 1) {
        hash_word2.delete(char);
      } else {
        hash_word2.set(char, [hash_word2.get(char)[0] - 1, idx2]);
      }
      // delete the character from hash_word2 is it is 1
      if (hash_word2.get(char)[0] === 1) {
        hash_word2.delete(char);
      } else {
        hash_word2.set(char, [hash_word2.get(char)[0] - 1, idx2]);
      }
      // check swap char is sin hash_word1
      if (hash_word1.has(char)) {
        hash_word1.set(char, [hash_word1.get(char)[0] + 1, idx2]);
      } else {
        hash_word1.set(char, [1, idx2]);
      }

      break;
    }
  }
  console.log(hash_word1, hash_word2);
  // check if both the hash map size are same
  if (hash_word1.size === hash_word2.size) return true;

  return false;
};

("adba");
("adbc");
word1 = "ab";
word2 = "abcc";
console.log(isItPossible(word1, word2));
