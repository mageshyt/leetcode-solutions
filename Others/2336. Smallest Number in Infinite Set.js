`You have a set which contains all positive integers [1, 2, 3, 4, 5, ...].

Implement the SmallestInfiniteSet class:

SmallestInfiniteSet() Initializes the SmallestInfiniteSet object to contain all positive integers.
int popSmallest() Removes and returns the smallest integer contained in the infinite set.
void addBack(int num) Adds a positive integer num back into the infinite set, if it is not already in the infinite set.
 

Example 1:

Input
["SmallestInfiniteSet", "addBack", "popSmallest", "popSmallest", "popSmallest", "addBack", "popSmallest", "popSmallest", "popSmallest"]
[[], [2], [], [], [], [1], [], [], []]
Output
[null, null, 1, 2, 3, null, 1, 4, 5]

Explanation
SmallestInfiniteSet smallestInfiniteSet = new SmallestInfiniteSet();
smallestInfiniteSet.addBack(2);    // 2 is already in the set, so no change is made.
smallestInfiniteSet.popSmallest(); // return 1, since 1 is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 2, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 3, and remove it from the set.
smallestInfiniteSet.addBack(1);    // 1 is added back to the set.
smallestInfiniteSet.popSmallest(); // return 1, since 1 was added back to the set and
                                   // is the smallest number, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 4, and remove it from the set.
smallestInfiniteSet.popSmallest(); // return 5, and remove it from the set.
`;

class SmallestInfiniteSet {
  constructor() {
    this.arr = [];
    this.remove = 1;
  }

  addBack(n) {
    if (this.remove > n && !this.arr.includes(n)) {
      this.arr.push(n);
    }
  }
  popSmallest() {
    if (this.arr.length) {
      this.arr.sort((a, b) => b - a);
      return this.arr.pop();
    }
    this.remove++;

    return this.remove - 1;
  }
}

s = new SmallestInfiniteSet();
console.log(s.popSmallest());
console.log(s.popSmallest());
console.log(s.popSmallest());
s.addBack(1);
s.popSmallest();
s.popSmallest();
s.popSmallest();
s.addBack(2);
console.log(s);
s.addBack(3);
console.log(s);
console.log(s.popSmallest());
