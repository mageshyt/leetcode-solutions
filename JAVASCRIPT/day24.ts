`2631. Group By`;

declare global {
  interface Array<T> {
    groupBy(fn: (item: T) => string): Record<string, T[]>;
  }
}

Array.prototype.groupBy = function (fn) {
  const result = {};

  for (const item of this) {
    const key = fn(item);

    if (result[key]) {
      result[key].push(item);
    } else {
      result[key] = [item];
    }
  }

  return result;
};
