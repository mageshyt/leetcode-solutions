
  for (let i = 0; i <= word2.length; i++) {
    table[word1.length][i] = word2.length - i;
  }
  for (let i = 0; i <= word1.length; i++) {
    table[i][word2.length] = word1.length - i;
  }