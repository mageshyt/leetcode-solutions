`520. Detect Capital
Easy

1376

340

Add to List

Share
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.

Example 1:

Input: word = "USA"
Output: true
Example 2:

Input: word = "FlaG"
Output: false`;
const detectCapitalUse = (word) => {
  let capitalCount = 0;
  let smallCount = 0;
  for (let i = 0; i < word.length; i++) {
    const currentChar = word[i];
    // if currentChar is capital, increment capitalCount
    if (currentChar === currentChar.toUpperCase()) {
      capitalCount++;
    }
    if (currentChar === currentChar.toLowerCase()) {
      smallCount++;
    }
  }

  return word.length === capitalCount
    ? true
    : false || word.length === smallCount
    ? true
    : false ||
      (word[0] === word[0].toUpperCase() &&
        capitalCount === 1 &&
        smallCount === word.length - 1)
    ? true
    : false;
};

word = "Google";
console.log(detectCapital(word));


  ```
  First we will count the capitals and small letters.
    Now we will check first condition.
        If the number of capital letter is equal to length of the word,then return true.
        Ex: 'APPLE'
        * Here all the letter are capital letter so we will return true.
    Now we will check second condition.
        If the number of small letter is equal to length of the word,then return true. which mean the given word has no capital letters.
        Ex: "leetcode"
        * here all the letter are small ,so we will return true.
    Now we will check third condition.
        If the first letter of the word is capital, then remianing letters should be small letters, then we will return true.
        Ex: "Google"
        * First letter is G, then remaining letters should be o,l,e,t,c,o,d. So we will return true.
    

  ```;