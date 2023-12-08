//--- Day 4: Scratchcards ---

const fs = require("fs");
const path = require("path");
const input = fs.readFileSync(path.resolve(__dirname, "testcase.txt"), "utf8");
const inputArray = input.split("\n");

const Scratchcards = (inputs: String[]): Number => {
  let wonHash = new Map();

  for (let i = 0; i < inputs.length; i++) {
    const cardId: String = "Card " + (i + 1);
    let line = inputs[i];

    // remove the cardID from the input string
    line = line.split(":").slice(1).join("").trim();
    // console.log(">> line ", cardId, line);

    const result = helper2(line);

    //  increment the the count of cards won
    // console.log("checking ", cardId, wonHash);
    wonHash.set(cardId, wonHash.get(cardId) + 1 || 1);

    // console.log(`>> result of  ${cardId}`, result);
    console.log(wonHash);
    // start the loop from next card
    let start = i + 1;
    let end = i + 1 + result;

    const wonCounts = wonHash.get(cardId) || 1;
    console.log(">> wonCounts ", wonCounts);
    for (let k = 0; k < wonCounts; k++) {
      for (let j = start; j < end; j++) {
        const wonCardId: String = "Card " + (j + 1);
        wonHash.set(wonCardId, wonHash.get(wonCardId) + 1 || 1);
      }
    }

    // if (!wonHash.has(i + 1)) wonHash.set(i + 1, 1);
  }

  let res = 0;

  for (let [key, value] of wonHash) {
    res += value;
  }

  return res;
};

// part 1
const helper1 = (line: String) => {
  let ans = 0;
  let tickets = line.split("|");
  // left is winning ticket and right is the our ticket

  const winningTicket = tickets[0].split(" ");

  const ourTicket = tickets[1].split(" ");

  for (let i = 0; i < ourTicket.length; i++) {
    const ourNum = ourTicket[i];

    if (!ourNum) continue;
    if (winningTicket.includes(ourNum)) {
      ans = ans >= 1 ? ans * 2 : 1;
    }
  }

  // console.log(winningTicket, ourTicket);
  return ans;
};

// part 2

const helper2 = (line: String) => {
  let ans = 0;
  let tickets = line.split("|");
  // left is winning ticket and right is the our ticket

  const winningTicket = tickets[0].split(" ");

  const ourTicket = tickets[1].split(" ");

  const wonHash = new Map();

  let winningNums = 0;

  for (let i = 0; i < ourTicket.length; i++) {
    const ourNum = ourTicket[i];

    if (!ourNum) continue;

    if (winningTicket.includes(ourNum)) {
      winningNums++;
    }
  }

  // console.log(winningNums, wonHash);

  return winningNums;
};
console.log(Scratchcards(inputArray));

// console.log(helper1(inputArray[0]));
