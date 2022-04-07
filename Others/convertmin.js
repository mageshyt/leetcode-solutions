const ConvertToMinValue = (N, K, num) => {
  //! n--> of digits
  //! k--> of digits
  //! num--> of digits
  if (N === 1) return 0; // !Edge case

  let converted_num = num.toString().split("").map(Number);

  let left = 1;
  let right = 2;
  let count = 0;

  if (converted_num[0] !== 1) {
    //! if the first digit is not 1 then make it as 1 so we will get smallest possible number
    converted_num[0] = 1;

    count++;
  }

  while (left < converted_num.length + 1 && count !== K) {
    const left_val = converted_num[left];
    const right_val = converted_num[right] || 0;
    if (left_val > right_val) converted_num[left] = 0;
    // ! if left is greater than right, then we can replace left with 0
    else if (left_val === 0 && right_val !== 0) converted_num[right] = 0;
    else if (left_val < right_val) converted_num[left] = 0;
    // ! if left is less than right, then we can replace right with 0
    left++;
    right++;
    count++;
  }
  console.log(converted_num);
  return converted_num.join("");
};
console.log(ConvertToMinValue(6, 2, 12054));
console.log(ConvertToMinValue(3, 3, 900));
console.log(ConvertToMinValue(1, 1, 8));
console.log(ConvertToMinValue(4, 3, 1942));
console.log(ConvertToMinValue(5, 2, 924151));
console.log(ConvertToMinValue(6, 8, 12054));
