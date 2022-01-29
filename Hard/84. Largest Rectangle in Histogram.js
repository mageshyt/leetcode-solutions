`Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
`;
const largestRectangleArea = (height) => {
  height.push(0);
  let stack = [];
  let maxArea = 0;
  for (let i = 0; i < height.length; i++) {
    const height_start = i;
    const current_height = height[i];
    while (stack.length && stack[stack.length - 1][1] > current_height) {
      const [position, height] = stack.pop(); //* we are taking out the position and height
      const area = height * (i - position);

      // ! we can find the Area by height x width;
      `
              Example:
                height = [2,1,5,6,2,3]
                i = 6
                stack = [3,5]
                height[3] = 2
                height[5] = 6
                area = 2*(6-3) = 12
                
              `;
      maxArea = Math.max(maxArea, area); // ! we will compare the area with the maxArea
      height_start = position;
    }
    stack.push([height_start, current_height]);
  }
  return maxArea;
};
height = [2, 1, 2];
const res = largestRectangleArea(height);
console.log(res);
