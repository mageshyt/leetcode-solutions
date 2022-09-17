`You are playing a game that contains multiple characters, and each of the characters has two main properties: attack and defense. You are given a 2D integer array properties where properties[i] = [attacki, defensei] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. More formally, a character i is said to be weak if there exists another character j where attackj > attacki and defensej > defensei.

Return the number of weak characters.

 

Example 1:

Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character has strictly greater attack and defense than the other.
Example 2:

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has a strictly greater attack and defense.
Example 3:

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has a strictly greater attack and defense.
`;

const numberOfWeakCharacters = (properties) => {
  let count = 0;
  properties.sort((a, b) => (a[0] == b[0] ? a[1] - b[1] : b[0] - a[0])); // sort by attack and defense
  let max = 0; // max defense
  for (let [attack, defense] of properties) {
    if (defense < max) count++;
    else max = defense;
  }
  return count;
};

console.log(
  numberOfWeakCharacters([
    [5, 5],
    [6, 3],
    [3, 6],
  ])
);
