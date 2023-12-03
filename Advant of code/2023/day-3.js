const fs = require("fs");

const path = require("path");

const data = fs.readFileSync(path.join(__dirname, "testcase.txt"), "utf8");
const lines = data.trim().split("\n");
console.log("👉 leans", lines);

const n = lines.length;
const m = lines[0].length;

console.log("👉 n", n);
console.log("👉 m", m);

const is_symbol = (i, j) => {
  if (!(0 <= i && i < n && 0 <= j && j < m)) {
    return false;
  }

  return lines[i][j] !== "." && !isNaN(lines[i][j]);
};

let ans = 0;

for (let i = 0; i < lines.length; i++) {
  let start = 0;
  let j = 0;

  while (j < m) {
    start = j;
    let num = "";

    while (j < m && !isNaN(lines[i][j])) {
      num += lines[i][j];
      j++;
    }

    if (num === "") {
      j++;
      continue;
    }

    const numInt = parseInt(num);

    // Number ended, look around
    if (is_symbol(i, start - 1) || is_symbol(i, j)) {
      ans += numInt;
      continue;
    }

    for (let k = start - 1; k <= j; k++) {
      if (is_symbol(i - 1, k) || is_symbol(i + 1, k)) {
        ans += numInt;
        break;
      }
    }
  }
}

console.log(ans);
