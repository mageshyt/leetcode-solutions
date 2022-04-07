`Given an array of strings words, return the words that can be typed using letters of the alphabet on only one row of American keyboard like the image below.

In the American keyboard:

the first row consists of the characters "qwertyuiop",
the second row consists of the characters "asdfghjkl", and
the third row consists of the characters "zxcvbnm".

Example 1:

Input: words = ["Hello","Alaska","Dad","Peace"]
Output: ["Alaska","Dad"]
Example 2:

Input: words = ["omk"]
Output: []
Example 3:

Input: words = ["adsdf","sfd"]
Output: ["adsdf","sfd"]

`;

`
step 1:
get the first letters of the word and check were in the row 

`;
const getRow = (char) => {
  const row1 = {
    q: true,
    w: true,
    e: true,
    r: true,
    t: true,
    y: true,
    u: true,
    i: true,
    o: true,
    p: true,
    Q: true,
    W: true,
    E: true,
    R: true,
    T: true,
    Y: true,
    U: true,
    I: true,
    O: true,
    P: true,
  };
  const row2 = {
    a: true,
    s: true,
    d: true,
    f: true,
    g: true,
    h: true,
    j: true,
    k: true,
    l: true,
    A: true,
    S: true,
    D: true,
    F: true,
    G: true,
    H: true,
    J: true,
    K: true,
    L: true,
  };
  const row3 = {
    z: true,
    x: true,
    c: true,
    v: true,
    b: true,
    n: true,
    m: true,
    Z: true,
    X: true,
    C: true,
    V: true,
    B: true,
    N: true,
    M: true,
  };
  // ! here we are getting the row for the first letter of the word
  if (row1[char]) {
    return row1;
  } else if (row2[char]) {
    return row2;
  } else {
    return row3;
  }
};

const findWords = (array) => {
  const result = [];

  for (let word of array) {
    const first_letter = word[0].toLowerCase(); // ! converting first letter to lower case and get the row for it

    const row = getRow(first_letter);
    // console.log({row});

    let str = "";

    let start = 0;
    let end = word.length - 1;
    while (start <= end) {
      if (row[word[start].toLowerCase()]) {
        // * if the letter in the specified row then add to the str
        str += word[start];
      }
      start++;
    }

    if (str === word) {
      // ! here we are check is the str is qual or not to the word so that we can find it if the word is form that row are not ,if the word is not qual then it means not form the row
      result.push(word);
    }
  }
  return result;
};

words = ["adsdf", "sfd"];
console.log(findWords(words));
