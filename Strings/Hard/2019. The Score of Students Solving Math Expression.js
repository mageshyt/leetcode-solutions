`
You are given a string s that contains digits 0-9, addition symbols '+', and multiplication symbols '*' only, representing a valid math expression of single digit numbers (e.g., 3+5*2). This expression was given to n elementary school students. The students were instructed to get the answer of the expression by following this order of operations:

Compute multiplication, reading from left to right; Then,
Compute addition, reading from left to right.
You are given an integer array answers of length n, which are the submitted answers of the students in no particular order. You are asked to grade the answers, by following these rules:

If an answer equals the correct answer of the expression, this student will be rewarded 5 points;
Otherwise, if the answer could be interpreted as if the student applied the operators in the wrong order but had correct arithmetic, this student will be rewarded 2 points;
Otherwise, this student will be rewarded 0 points.
Return the sum of the points of the students.

 

Example 1:


`;
const left_to_right = (s, answers) => {
  const converted_s = s.split("").map((x) => {
    if (x === "+" || x === "*") {
      return x;
    }
    return parseInt(x);
  });
  let result = 0;
  let left = converted_s.length - 2;

  while (left >= 0) {
    let right = left + 1;
    const current = converted_s[left];
    if (current === "*") {
      result = converted_s[left - 1] * converted_s[right];

      converted_s[left - 1] = result;
      left -= 2;
    }
    if (current === "+") {
      result = converted_s[left - 1] + converted_s[right];

      converted_s[left - 1] = result;
      left -= 2;
    }
  }
  return result;
};
const right_to_left = (s, answers) => {
  const converted_s = s.split("").map((x) => {
    if (x === "+" || x === "*") {
      return x;
    }
    return parseInt(x);
  });
  let result = 0;
  let right = 1;

  while (right < converted_s.length) {
    let left = right - 1;

    const current = converted_s[right];
    // if (counter <= 10) {
    //   console.log({
    //     current,
    //     left: converted_s[left],
    //     right: converted_s[right + 1],
    //     result,
    //   });
    // }

    if (current === "*") {
      result = converted_s[left] * converted_s[right + 1];

      converted_s[right + 1] = result;
      right += 2;
    }
    if (current === "+") {
      result = converted_s[left] + converted_s[right + 1];

      converted_s[right + 1] = result;
      //   console.log("result", result, converted_s);
      right += 2;
    }
  }
  return result;
};
const scoreOfStudents = (s, answers) => {
  correct_ans = left_to_right(s, answers);
  ans_right_to_left = right_to_left(s, answers);
  console.log({ correct_ans, ans_right_to_left });
  let score = 0;
  answers.forEach((answer) => {
    if (answer === correct_ans) {
      score += 5;
    } else if (answer === ans_right_to_left) {
      score += 2;
    }
  });
  return score;
};

s = "1+2*3+4";
answers = [13, 21, 11, 15];
console.log(scoreOfStudents(s, answers));
