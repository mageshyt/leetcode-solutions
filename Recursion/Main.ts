class Main {
  message(i: number): void {
    if (i == 0) return;
    console.log("Hello World");
    this.message(i - 1);
  }
  
}

new Main().message(10);
