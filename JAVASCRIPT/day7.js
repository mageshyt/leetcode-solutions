`2629. Function Composition
`;

//   function programming
var compose = function (functions) {
  return function (x) {
    for (const fn of functions.reverse()) {
      x = fn(x);
    }

    return x;
  };
};

// declarative programming
var compose = function (functions) {
  return function (x) {
    return functions.reduceRight((acc, fn) => fn(acc), x);
  };
};
const fn = compose([(x) => x + 1, (x) => 2 * x]);
console.log(fn(4)); // 9
