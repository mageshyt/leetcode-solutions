class MinStack {
  stack: number[] = [];
  minStack: number[] = [];
  constructor() {
    this.stack = [];
    this.minStack = [];
  }

  push(val: number): void {
    // first push to stack
    this.stack.push(val);
    const min_value = Math.min(
      val,
      this.minStack[this.minStack.length - 1] || val
    );
    this.minStack.push(min_value);
  }

  pop(): void {
    this.stack.pop();
    this.minStack.pop();
  }

  top(): number {
    return this.stack[this.stack.length - 1];
  }

  getMin(): number {
    return this.minStack[this.minStack.length - 1] || 0;
  }
}
