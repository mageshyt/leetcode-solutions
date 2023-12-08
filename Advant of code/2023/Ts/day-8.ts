

const data = fs.readFileSync("testcase.txt", "utf8");
// Rest of your code
import fs from "fs";
const path = require("path");
const input = fs.readFileSync(path.resolve(__dirname, "testcase.txt"), "utf8");
const inputArray = input.split("\n");