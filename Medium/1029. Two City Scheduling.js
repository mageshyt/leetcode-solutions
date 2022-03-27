const twoCitySchedCost = (costs) => {
  costs.sort((a, b) => a[0] - a[1] - b[0] + b[1]);
  let sum = 0;
  let mid = costs.length / 2;
  for (let i = 0; i < mid; i++) {
    sum += costs[i][0];
  }
  for (let i = mid; i < costs.length; i++) {
    sum += costs[i][1];
  }
  return sum;
};
console.log(
  twoCitySchedCost([
    [10, 20],
    [30, 200],
    [400, 50],
    [30, 20],
  ])
);
