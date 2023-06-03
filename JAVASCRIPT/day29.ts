`2648. Generate Fibonacci Sequence
https://www.codewars.com/kata/55f5efd21ad2b48895000040/train/javascript`;

function* fibGenerator(): Generator<number, any, number> {
  let a = 0;
  let b = 1;
  while (true) {
    yield a;
    [a, b] = [b, a + b];
  }
}
