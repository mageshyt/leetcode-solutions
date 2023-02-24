class Main {
  message(i: number): void {
    if (i == 0) return;
    console.log("Hello World");
    this.message(i - 1);
  }

  fib(n: number, hash = {}): number {
    if (n == 0) return 0;
    if (n == 1) return 1;
    if (hash[n]) return hash[n];
    hash[n] = this.fib(n - 1) + this.fib(n - 2);

    return hash[n];
  }
}
const main = new Main();

console.log(main.fib(100));
