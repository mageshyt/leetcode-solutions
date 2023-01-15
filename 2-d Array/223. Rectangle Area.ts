`Given the coordinates of two rectilinear rectangles in a 2D plane, return the total area covered by the two rectangles.

The first rectangle is defined by its bottom-left corner (ax1, ay1) and its top-right corner (ax2, ay2).

The second rectangle is defined by its bottom-left corner (bx1, by1) and its top-right corner (bx2, by2).

 

Example 1:

Rectangle Area
Input: ax1 = -3, ay1 = 0, ax2 = 3, ay2 = 4, bx1 = 0, by1 = -1, bx2 = 9, by2 = 2
Output: 45
Example 2:

Input: ax1 = -2, ay1 = -2, ax2 = 2, ay2 = 2, bx1 = -2, by1 = -2, bx2 = 2, by2 = 2
Output: 16
 

Constraints:

-104 <= ax1 <= ax2 <= 104
-104 <= ay1 <= ay2 <= 104
-104 <= bx1 <= bx2 <= 104
-104 <= by1 <= by2 <= 104`;

const computeArea = (
  ax1: number,
  ay1: number,
  ax2: number,
  ay2: number,
  bx1: number,
  by1: number,
  bx2: number,
  by2: number
): number => {
  let result: number = 0;

  // Rectangle one Area formula is (ax2-ax1) * (ay2-ay1a)
  const area1 = (ax2 - ax1) * (ay2 - ay1);
  // Rectangle two Area formula is (bx2-bx1) * (by2-by1)
  const area2 = (bx2 - bx1) * (by2 - by1);
  console.log(area1, area2);

  // if the two rectangles do not overlap

  if (ax2 <= bx1 || bx2 <= ax1 || ay2 <= by1 || by2 <= ay1) {
    result = area1 + area2;
  } else {
    // if the two rectangles overlap
    const cord_1 = [Math.min(bx2, by2), Math.min(ax2, ay2)];
    const cord_2 = [Math.max(ax1, ay1), Math.max(bx1, by1)];

    const overlapsArea = (cord_1[0] - cord_2[0]) * (cord_1[1] - cord_2[1]);
    console.log(overlapsArea);

    result = area1 + area2 - overlapsArea;
  }

  return result;
};

console.log(computeArea(-3, 0, 3, 4, 0, -1, 9, 2));

console.log(computeArea(-2, -2, 2, 2, -2, -2, 2, 2));
