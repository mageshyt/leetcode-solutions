`An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

 

Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.
Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]`;

const floodFill = (image, sr, sc, newColor) => {
  const directions = [
    [1, 0], // Right
    [-1, 0], // Left
    [0, 1], // up
    [0, -1], // down
  ];
  const initialPixel = image[sr][sc];
  const visited = new Map();
  const dfs = (row, col, color) => {
    const key = `${row}-${col}`;
    if (visited.get(key)) return;
    visited.set(key, true);
    const pixel = image[row][col];
    if (pixel !== initialPixel) return;
    image[row][col] = newColor;
    for (let [dr, dc] of directions) {
      const newRow = dr + row;
      const newCol = dc + col;
      if (
        newRow >= 0 &&
        newRow < image.length &&
        newCol >= 0 &&
        newCol < image[0].length
      )
        dfs(newRow, newCol, color);
    }
  };
  dfs(sr, sc, image[sr][sc]);
  return image;
};

const image = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1],
];
console.log(floodFill(image, 1, 1, 2));

const image2 = [
  [0, 0, 0],
  [0, 0, 0],
];
console.log(floodFill(image2, 0, 0, 2));
