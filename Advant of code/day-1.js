// read the file from testcase.txt
const fs = require("fs");
const path = require("path");
const input = fs.readFileSync(path.join(__dirname, "testcase.txt"), "utf8");
// split the input into array
const inputArray = input.split("\n");

const formateInput = inputArray.map((item) => {
  if (item.length === 0) return "";
  return parseInt(item);
});

`For example, suppose the Elves finish writing their items' Calories and end up with the following list:

1000
2000
3000

4000

5000
6000

7000
8000
9000

10000
This list represents the Calories of the food carried by five Elves:

The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total of 6000 Calories.
The second Elf is carrying one food item with 4000 Calories.
The third Elf is carrying food with 5000 and 6000 Calories, a total of 11000 Calories.
The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total of 24000 Calories.
The fifth Elf is carrying one food item with 10000 Calories.
`;

const maxCalories = (array) => {
  let max = 0;
  let sum = 0;
  const values = [];

  for (let i = 0; i <= array.length; i++) {
    if (i === array.length) values.push(sum);
    if (array[i] === "") {
      values.push(sum);
      sum = 0;
      continue;
    } else {
      sum += parseInt(array[i]);
      if (sum > max) max = sum;
      if (sum < 0) sum = 0;
    }
  }
  // sum of top 3
  values.sort((a, b) => b - a);
  console.log(values);
  return values[0] + values[1] + values[2];
};
console.log(maxCalories(formateInput));
