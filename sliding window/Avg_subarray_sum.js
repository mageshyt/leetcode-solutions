`   


`;

const avg_subarray_sum = (arr, k) => {
  const result = [];
  const queue = [];
  let sum = 0;
  for (let i = 0; i < arr.length; i++) {
    if (queue.length !== k) {
      queue.push(arr[i]);
      sum += arr[i];
    }
    if (queue.length === k) {
      result.push(sum / k);
      const pop = queue.shift();
      sum -= pop;
    }
  }
  return result;
};
console.log(avg_subarray_sum([1, 2, 3, 4, 5], 3));

console.log(avg_subarray_sum([1, 3, 2, 6, -1, 4, 1, 8, 2], 5));
