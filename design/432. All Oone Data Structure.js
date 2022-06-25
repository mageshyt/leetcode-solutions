`Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, 
remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"`;

class AllOne {
  constructor() {
    this.map = new Map();
  }

  inc(key) {
    if (!this.map.has(key)) {
      this.map.set(key, 1);
    } else {
      this.map.set(key, this.map.get(key) + 1);
    }
  }

  dec(key) {
    if (this.map.has(key)) {
      if (this.map.get(key) === 1) {
        this.map.delete(key);
      } else {
        this.map.set(key, this.map.get(key) - 1);
      }
    }
  }
  getMaxKey() {
    let max = Number.MIN_SAFE_INTEGER;
    let maxKey = "";
    for (let [key, value] of this.map) {
      if (value > max) {
        max = value;
        maxKey = key;
      }
    }
    return maxKey;
  }
  getMinKey() {
    let min = Number.MAX_SAFE_INTEGER;
    let min_key = "";
    for (let [key, value] of this.map) {
      if (value < min) {
        min = value;
        min_key = key;
      }
    }
    return min_key;
  }
}

const solve = new AllOne();
solve.inc("hello");
solve.inc("hello");
console.log(solve.getMaxKey()); // return "hello"
solve.getMinKey(); // return "hello"
solve.dec("hello");
solve.inc("Leet");
solve.inc("Leet");
console.log(solve.getMaxKey()); // return "hello"
console.log("min", solve.getMinKey()); // return "hello"
console.log(solve);
