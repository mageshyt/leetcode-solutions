const minDominoRotations = (top, bottom) => {
  //! 4 counters
  let count1 = 0;
  let count2 = 0;
  let count3 = 0;
  let count4 = 0;
  //! conditions 1
  let num1 = top[0];
  let num2 = bottom[0];

  //! loop through top
  for (let i = 0; i < top.length; i++) {
    const curr_top = top[i];
    const curr_bottom = bottom[i];
    if (count1 !== Infinity) {
      if (curr_top === num1) {
      } else if (curr_bottom === num1) {
        count1++;
      } else {
        count1 = Infinity;
      }
    }
    //! for count 2
    if (count2 !== Infinity) {
      if (curr_bottom === num1) {
      } else if (curr_top === num1) {
        count2++;
      } else {
        count2 = Infinity;
      }
    }
    //! for count 3
    if (count3 !== Infinity) {
      if (curr_bottom === num2) {
      } else if (curr_top === num2) {
        count3++;
      } else {
        count3 = Infinity;
      }
    }
    //! for count 4
    if (count4 !== Infinity) {
      if (curr_top === num2) {
      } else if (curr_bottom === num2) {
        count4++;
      } else {
        count4 = Infinity;
      }
    }
  }
  //! return the minimum number of rotations
  console.log(count1, count2, count3, count4);
  const res = Math.min(Math.min(count1, count2), Math.min(count3, count4));
  return res === Infinity ? -1 : res;
};

console.log(minDominoRotations([2, 1, 2, 4, 2, 2], [5, 2, 6, 2, 3, 2]));
