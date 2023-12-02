const fs = require("fs");
const path = require("path");
const input = fs.readFileSync(path.join(__dirname, "testcase.txt"), "utf8");
// split the input into array
const inputArray = input.split("\n");
const CubeConundrum = (inputArray) => {
  let res = 0;

  for (let i = 0; i < inputArray.length; i++) {
    const games = inputArray[i];

    if (games.length === 0) continue;
    res += helper2(games, i + 1);
  }

  return res;
};

// Part 1
const helper1 = (str, idx) => {
  // now we need to convert the each and every game into array of set of cubes shows
  `
    only 12 red cubes, 13 green cubes, and 14 blue cubes
    ex:Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    to [[3,4],[1,2],[6,2]]
    `;

  const games = str
    .replace(`Game ${idx}:`, "")
    .split(";")
    .map((game) => {
      const cubes = game
        .trim()
        .split(",")
        .map((cube) => {
          const [num, color] = cube.trim().split(" ");

          return [parseInt(num), color];
        });

      return cubes;
    });
  console.log("👉 games", games);

  const cubeMap = new Map();

  cubeMap.set("red", 12);
  cubeMap.set("green", 13);
  cubeMap.set("blue", 14);

  for (let game of games) {
    for (let cube of game) {
      const [num, color] = cube;

      // remaining cubes

      const availableCube = cubeMap.get(color);
      if (availableCube < num) return false;
    }
  }

  return true;
};

const helper2 = (str, idx) => {
  const cubeMap = new Map();
  const games = str
    .replace(`Game ${idx}:`, "")
    .split(";")
    .map((game) => {
      const cubes = game
        .trim()
        .split(",")
        .map((cube) => {
          const [num, color] = cube.trim().split(" ");

          cubeMap.set(color, [...(cubeMap.get(color) || []), parseInt(num)]);

          return [parseInt(num), color];
        });

      return cubes;
    });

  //   console.log("👉 cubes", cubeMap);

  let power = 1;

  for (let [key, value] of cubeMap.entries()) {
    // get the max value

    const maxValue = Math.max(...value);
    // console.log("👉 max in " + key + maxValue);

    power *= maxValue;
  }

  console.log("👉 power", power);
  return power;
};
console.log("👉 ", CubeConundrum(inputArray));
