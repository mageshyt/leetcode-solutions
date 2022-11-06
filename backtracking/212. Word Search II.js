`Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]
Example 2:


Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
 `;

const findWords = (board, words) => {
  const rows = board.length;
  const cols = board[0].length;

  const start_char_map = new Map();

  for (let i = 0; i < rows; i++) {
    for (let j = 0; j < cols; j++) {
      const curr_char = board[i][j];
      if (!start_char_map.has(curr_char)) {
        start_char_map.set(curr_char, []);
      }
      start_char_map.get(curr_char).push([i, j]);
    }
  }

  const directions = [
    [1, 0], // Right
    [-1, 0], // Left
    [0, 1], // up
    [0, -1], // down
  ];

  const visited = new Map();
  const dfs = (row, col, index, word) => {
    // base case
    if (index === word.length) return true;

    // check if the current cell is out of bounds or if the current cell is not equal to the current letter in the word
    if (row < 0 || row >= rows) return false;

    //! case two - out of bounds for col

    if (col < 0 || col >= cols) return false;

    //! case three - the current cell is not equal to the current letter in the word

    if (board[row][col] !== word[index]) return false;

    // check if the current cell has been visited before
    if (visited.has(`${row}-${col}`)) return false;

    // mark the current cell as visited
    visited.set(`${row}-${col}`, true);
    // explore the neighbors of the current cell
    for (let i = 0; i < directions.length; i++) {
      const [rowOffset, colOffset] = directions[i];
      const newRow = row + rowOffset;
      const newCol = col + colOffset;
      if (dfs(newRow, newCol, index + 1, word)) return true;
    }
    // unmark the current cell as visited
    visited.delete(`${row}-${col}`);
    return false;
  };

  const res = [];

  // loop through the words array
  for (let i = 0; i < words.length; i++) {
    const word = words[i];
    const start_char = word[0];
    const start_coords = start_char_map.get(start_char);
    if (start_char_map.has(start_char)) {
      start_coords.forEach((coord) => {
        const [row, col] = coord;
        if (dfs(row, col, 0, word)) {
          if (!res.includes(word)) res.push(word);
        }
      });
      //! reset the visited map
      visited.clear();
    }
  }

  return res;
};

//! optimized solution
const directions = [
  [1, 0], // Right
  [-1, 0], // Left
  [0, 1], // up
  [0, -1], // down
];
const findWords2 = (board, words) => {
  let res = [];

  const root = buildTrie(words);
  for (let row = 0; row < board.length; row++) {
    for (let col = 0; col < board[0].length; col++) {
      dfs(root, row, col, board, res);
    }
  }

  return res;
};
const dfs = (node, row, col, board, res) => {
  if (node.end) {
    res.push(node.end);
    node.end = null; // make sure only print one time for each word
  }

  if (row < 0 || row >= board.length || col < 0 || col >= board[0].length)
    return;
  if (!node[board[row][col]]) return;

  const c = board[row][col];
  board[row][col] = "#"; // mark visited
  dfs(node[c], row + 1, col, board, res); // up
  dfs(node[c], row - 1, col, board, res); // down
  dfs(node[c], row, col + 1, board, res); // right
  dfs(node[c], row, col - 1, board, res); // left
  board[row][col] = c; // reset - back track
};

const buildTrie = (words) => {
  const root = {};
  for (let word of words) {
    let pointer = root; // here 'pointer' just a reference, that we use to go down from root till last child node

    for (let char of word) {
      if (!pointer[char]) pointer[char] = {}; // if we already have such node, lets ignore it creating and just move the pointer
      pointer = pointer[char];
    }
    pointer.end = word;
  }
  return root;
};
console.log(
  findWords2(
    [
      ["o", "a", "a", "n"],
      ["e", "t", "a", "e"],
      ["i", "h", "k", "r"],
      ["i", "f", "l", "v"],
    ],
    ["oath", "pea", "eat", "rain"]
  )
);
