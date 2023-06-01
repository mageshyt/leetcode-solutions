`2695. Array Wrapper`;

class ArrayWrapper {
  nums: number[];
  constructor(nums: number[]) {
    this.nums = nums;
  }

  valueOf() {
    if (this.nums.length == 0) return 0;

    return this.nums.reduce((a, b) => a + b, 0);
  }

  toString() {
    const flat = this.nums.flat();

    return "[" + flat.join(", ") + "]";
  }
}

const obj1 = new ArrayWrapper([1, 2]);
const obj2 = new ArrayWrapper([3, 4, 5]);
console.log(obj1.toString());
