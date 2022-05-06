` You are given an integer N. You have to perform the following operation on N until N-1.
• Pick any integer X such that N is divisible by X. Divide N by X. If X is even, you get A points. If X
is odd, you get B points.
Find the maximum number of points
`;

const divisionGame = (N, A, B) => {
  let MaxPoints = 0;
  for (let i = 1; i < N; i++) {
    if (N % i === 0) {
      let points = 0;
      if (i % 2 === 0) {
        points = A;
      } else {
        points = B;
      }
      console.log(i, points);
      MaxPoints = Math.max(MaxPoints, points);
    }
  }
  return MaxPoints;
};

console.log(divisionGame(10, 2, 3));
