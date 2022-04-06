const minMovesToSeat = (seats, students) => {
  let min = 0;
  //! sort the seats
  seats.sort((a, b) => a - b);
  students.sort((a, b) => a - b);
  //! loop through the students
  students.forEach((pos, idx) => {
    const moves = Math.abs(pos - seats[idx]);
    min += moves;
  });
  return min;
};
(seats = [4, 1, 5, 9]), (students = [1, 3, 2, 6]);
console.log(minMovesToSeat(seats, students));
