// Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD, return the day number of the year.

// Example 1:

// Input: date = "2019-01-09"
// Output: 9
// Explanation: Given date is the 9th day of the year in 2019.
// Example 2:

// Input: date = "2019-02-10"
// Output: 41
// Example 3:

// Input: date = "2003-03-01"
// Output: 60
// Example 4:

// Input: date = "2004-03-01"
// Output: 61

// ! steps:
// * step 1:
"remove '-' from the input";

var dayOfYear = function (date) {
  let converted = date.split("-");
 const  Leap_months = {
    0: 0,
    1: 31,
    2: 59,
    3: 90,
    4: 120,
    5: 151,
    6: 181,
    7: 212,
    8: 243,
    9: 273,
    10: 304,
    11: 334,
    12: 365,
  };
  if (Number(converted[0]) % 4 !== 0) {
    return Leap_months[Number(converted[1]) - 1] + Number(converted[2]);
  } else {
    if (Number(converted[1] > 2)) {
      return Leap_months[Number(converted[1]) - 1] + Number(converted[2]) + 1;
    } else {
      return Leap_months[Number(converted[1]) - 1] + Number(converted[2]);
    }
  }
};
date = "2016-02-09";
console.log(dayOfYear(date));
