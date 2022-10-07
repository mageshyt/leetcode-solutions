class MinStack {
  constructor() {
    this.stack = [];
    this.min = Number.MAX_VALUE;
  }

  push(val) {
    if (val < this.min || this.stack.length === 0) {
      this.min = val;
    }
    this.stack.push(val, this.min);
  }
  pop() {
    this.stack.pop();

    this.min = this.stack[this.stack.length - 2];

    return this.stack.pop();
  }

  top() {
    return this.stack[this.stack.length - 2];
  }

  getMin() {
    return this.stack[this.stack.length - 1];
  }
}

const s = new MinStack();

s.push(2);

s.push(-1);

s.push(3);

console.log(s.getMin());
console.log(s);
