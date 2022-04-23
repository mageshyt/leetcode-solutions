`Take any 4 digit number. If one of its digits
 divides the number fully, this digit is called digit
divider. The number is given a rating called “Digit Divider Rating”. Rating is 100 if all of its
digits are digit dividers. Rating is 75, 50, 25, or 0 if number of digit dividers it has is 3, 2, 1 or
0.`;

const Digit_Divider_Rating = (n) => {
  const split = n
    .toString()
    .split("")
    .map((a) => parseInt(a));
  let count = 0;
  for (let num of split) {
    if (n % num === 0) {
      count++;
    }
  }
  if (count === 4) {
    return 100;
  }

  if (count === 3) {
    return 75;
  }
  if (count === 2) {
    return 50;
  }
  if (count === 1) {
    return 25;
  }
  if (count === 0) {
    return 0;
  }
};

console.log(Digit_Divider_Rating(8428));
