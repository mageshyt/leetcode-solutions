const binarySearch = (nums, start, end, target) => {
  if (start > end) return -1;
  let mid = Math.floor((start + end) / 2);
  if (nums[mid] === target) {
    return mid;
  }
  if (nums[mid] > target) {
    return binarySearch(nums, start, mid - 1, target);
  }
  if (nums[mid] < target) {
    return binarySearch(nums, mid + 1, end, target);
  }
  return -1;
};

const findFirstAndLastPosition = (nums, target) => {
  if (nums.length === 0) return [-1, -1];
  let findIdx = binarySearch(nums, 0, nums.length - 1, target);
  if (findIdx === -1) return [-1, -1]; //! if idx not found means then the target is not exists
  let start = findIdx;
  let end = findIdx;

  let temp1 = 0;
  while (start !== -1) {
    temp1 = start;
    start = binarySearch(nums, 0, start - 1, target);
  }
  start = temp1;

  let temp2 = 0;
  while (end !== -1) {
    temp2 = end;
    end = binarySearch(nums, end + 1, nums.length - 1, target);
  }
  end = temp2;
  return [start, end];
};

console.log(findFirstAndLastPosition([5, 7, 7, 8, 8, 10], 8));
