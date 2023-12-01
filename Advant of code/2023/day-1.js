// read the file from testcase.txt
const fs = require("fs");
const path = require("path");
const input = fs.readFileSync(path.join(__dirname, "testcase.txt"), "utf8");
// split the input into array
const inputArray = input.split("\n");

// console.log("👉 input", inputArray);

const findCalibrationSum = (array) => {
  let sum = 0;

  for (let calibration of array) {
    if (calibration.length === 0) continue;
    sum += helper2(calibration);
  }

  return sum;
};

// part 1
const helper = (str) => {
  // this function will return the 1 and last digit of the number

  let res = "";
  for (let char of str) {
    // check if the char is number

    if (!isNaN(char)) {
      res += char;
    }
  }
  return res.length === 1
    ? parseInt(res + res)
    : parseInt(res[0] + res[res.length - 1]);
};

// part 2

const helper2 = (str) => {
  // this function will return the 1 and last digit of the number

  const digits = new Map();

  digits.set("one", 1);
  digits.set("two", 2);
  digits.set("three", 3);
  digits.set("four", 4);
  digits.set("five", 5);
  digits.set("six", 6);
  digits.set("seven", 7);
  digits.set("eight", 8);
  digits.set("nine", 9);

  const startMap = new Map();

  startMap.set("o", ["one"]);
  startMap.set("t", ["two", "three"]);
  startMap.set("f", ["four", "five"]);
  startMap.set("s", ["six", "seven"]);
  startMap.set("e", ["eight"]);
  startMap.set("n", ["nine"]);

  let res = "";

  let i = 0;

  while (i < str.length) {
    // check if the char is number

    let word = "";
    let currentChar = str[i].toLowerCase();
    if (!isNaN(currentChar)) {
      res += currentChar;
      i++;
      continue;
    }

    const targets = startMap.get(currentChar);
    // if starting char is not in the map then skip
    if (!targets) {
      i++;
      continue;
    }

    for (let target of targets) {
      const currentWord = str.slice(i, i + target.length).toLowerCase();

      if (currentWord === target) {
        word = target;
        break;
      }
    }

    if (word.length === 0) {
      i++;
      continue;
    }

    res += digits.get(word);
    i += 1;
  }

  return res.length === 1
    ? parseInt(res + res)
    : parseInt(res[0] + res[res.length - 1]);
};

console.log(findCalibrationSum(inputArray));

// console.log(helper2("2four3threesxxvlfqfive4"));
