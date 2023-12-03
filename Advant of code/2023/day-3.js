//--- Day 3: Gear Ratios ---
const fs = require("fs");
const path = require("path");
const input = fs.readFileSync(path.resolve(__dirname, "testcase.txt"), "utf8");
const inputArray = input.split("\n");

rows = inputArray.length;
cols = inputArray[0].length;

const gondolaLift = (inputs) => {
  let res = 0;

  for (let i = 0; i < inputs.length; i++) {
    const line = inputs[i];

    res += helper1(line, i + 1);
  }

  return res;
};

// part 1

const helper1 = (line, i) => {
  let j = 0;
  let ans = 0;
  let start = 0;
  let digits = "0123456789";

  while (j < cols) {
    start = j;
    let num = "";

    while (j < cols && digits.includes(line[j])) {
      num += line[j];
      j++;
    }

    if (!num.length) {
      j++;
      continue;
    }

    const numInt = parseInt(num);

    // look at the ends

    if (is_symbol(i, start - 1) || is_symbol(i, j)) {
      ans += numInt;
      continue;
    }

    // look at the top and bottom

    for (let k = start; k <= j; k++) {
      if (is_symbol(i - 1, k) || is_symbol(i + 1, k)) {
        ans += numInt;
        break;
      }
    }
  }

  return ans;
};

const is_symbol = (i, j) => {
  if (i < 0 || i >= rows || j < 0 || j >= cols) return false;
  let digits = "0123456789";
  console.log("👉 line", inputArray[i][j]);
  if (!inputArray[i][j]) return false;
  return inputArray[i][j] !== "." && !digits.includes(inputArray[i][j]);
};

console.log("👉 ", gondolaLift(inputArray));
