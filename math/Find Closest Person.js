`
You are given three integers x, y, and z, representing the positions of three people on a number line:

x is the position of Person 1.
y is the position of Person 2.
z is the position of Person 3, who does not move.
Both Person 1 and Person 2 move toward Person 3 at the same speed.

Determine which person reaches Person 3 first:

Return 1 if Person 1 arrives first.
Return 2 if Person 2 arrives first.
Return 0 if both arrive at the same time.
Return the result accordingly.

 

Example 1:

Input: x = 2, y = 7, z = 4

Output: 1

Explanation:

Person 1 is at position 2 and can reach Person 3 (at position 4) in 2 steps.
Person 2 is at position 7 and can reach Person 3 in 3 steps.
Since Person 1 reaches Person 3 first, the output is 1.


`

const findClosest = (x, y, z) => {
  const person1Distance = Math.abs(x - z);
  const person2Distance = Math.abs(y - z);

  // if both distances are equal 
  if (person1Distance === person2Distance) {
    return 0;
  }

  return person1Distance < person2Distance ? 1 : 2;
}

console.log(findClosest(2, 7, 4)); // Output: 1
console.log(findClosest(3, 6, 5)); // Output: 2
