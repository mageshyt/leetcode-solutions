const paintWalls = (cost, time) => {
  const cache = new Map();

  const dp = (i, remaining) => {
    const key = `${i}-${remaining}`;

    //  base case
    if (remaining <= 0) {
      return 0;
    }

    if (i === cost.length) {
      return Infinity;
    }

    if (cache.has(key)) {
      return cache.get(key);
    }
    //  recursive case pain the wall or skip it

    const paint = cost[i] + dp(i + 1, remaining - 1 - time[i]); // for every one unit the free painter will pain the wall in 0 unit of time

    // skip the wall
    const skip = dp(i + 1, remaining);
    // our goal is to minimize the cost 
    const result = Math.min(paint, skip);

    cache.set(key, result);

    return result;
  };

  return dp(0, cost.length);
};

console.log("👉 pain wall " + paintWalls([1, 2, 3, 2], [1, 2, 3, 4]));
