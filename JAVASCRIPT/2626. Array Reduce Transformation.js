var reduce = function (nums, fn, init) {
  const res = [];

  let acc = init;

  for (let i = 0; i < nums.length; i++) {
    res.push(fn(acc, nums[i]));
    acc = res[i];
  }

  return res;
};

fn = function sum(accum, curr) {
  return accum + curr * curr;
};

console.log(reduce([1, 2, 3, 4], fn, 100));
