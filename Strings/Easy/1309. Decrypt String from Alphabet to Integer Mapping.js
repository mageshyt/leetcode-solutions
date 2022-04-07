`You are given a string s formed by digits and '#'. We want to map s to English lowercase characters as follows:

Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
Return the string formed after mapping.

The test cases are generated so that a unique mapping will always exist.

 

Example 1:
Input: s = "10#11#12"
Output: "jkab"
Explanation: "j" -> "10#" , "k" -> "11#" , "a" -> "1" , "b" -> "2".
Example 2:

Input: s = "1326#"
Output: "acz"`;

const freqAlphabets = (s) => {
  const s_array = s.split("");
  let res = "";
  for (let i = 0; i < s_array.length; i++) {
    const char = Number(s_array[i]);

    const next_char = s_array[i + 2];
    console.log({ curr: String.fromCharCode(char + 96), next: next_char });
    if (next_char !== "#") {
      const current_char = String.fromCharCode(parseInt(char) + 96);
      res += current_char;
    } else {
      const more = Number(char + s_array[i + 1]);
      const current_char = String.fromCharCode(parseInt(more) + 96);
      res += current_char;
      i += 2;
    }
  }
  return res;
};

console.log(freqAlphabets("10#11#12"));
console.log(String.fromCharCode(97 + 2));
