`You are implementing a program to use as your calendar. We can add a new event if adding the event will not cause a triple booking.

A triple booking happens when three events have some non-empty intersection (i.e., some moment is common to all the three events.).

The event can be represented as a pair of integers start and end that represents a booking on the half-open interval [start, end), the range of real numbers x such that start <= x < end.

Implement the MyCalendarTwo class:

MyCalendarTwo() Initializes the calendar object.
boolean book(int start, int end) Returns true if the event can be added to the calendar successfully without causing a triple booking. Otherwise, return false and do not add the event to the calendar.
 

Example 1:

Input
["MyCalendarTwo", "book", "book", "book", "book", "book", "book"]
[[], [10, 20], [50, 60], [10, 40], [5, 15], [5, 10], [25, 55]]
Output
[null, true, true, true, false, true, true]

Explanation
MyCalendarTwo myCalendarTwo = new MyCalendarTwo();
myCalendarTwo.book(10, 20); // return True, The event can be booked. 
myCalendarTwo.book(50, 60); // return True, The event can be booked. 
myCalendarTwo.book(10, 40); // return True, The event can be double booked. 
myCalendarTwo.book(5, 15);  // return False, The event cannot be booked, because it would result in a triple booking.
myCalendarTwo.book(5, 10); // return True, The event can be booked, as it does not use time 10 which is already double booked.
myCalendarTwo.book(25, 55); // return True, The event can be booked, as the time in [25, 40) will be double booked with the third event, the time [40, 50) will be single booked, and the time [50, 55) will be double booked with the second event.`;

class MyCalendarTwo {
  constructor() {
    this.map = new Map();
  }
  book(start, end) {
    this.map.set(start, (this.map.get(start) || 0) + 1);
    this.map.set(end, (this.map.get(end) || 0) - 1);
    let count = 0;
    for (let [_, v] of [...this.map.entries()].sort((a, b) => a[0] - b[0])) {
      console.log(_, v, count);
      count += v;
      if (count > 2) {
        //! undo the event
        this.map.set(start, (this.map.get(start) || 0) - 1);
        this.map.set(end, (this.map.get(end) || 0) + 1);
        return false;
      }
    }
    return true;
  }
}

// const myCalendarTwo = new MyCalendarTwo();
// console.log(myCalendarTwo.book(10, 20)); // return True, The event can be booked.
// console.log(myCalendarTwo.book(50, 60)); // return True, The event can be booked.
// console.log(myCalendarTwo.book(10, 40)); // return True, The event can be double booked.
// console.log(myCalendarTwo.book(5, 15)); // return False, The event cannot be booked, because it would result in a triple booking.

//! solution 2

class MyCalendarTwo2 {
  constructor() {
    this.overlaps = [];
    this.calendar = [];
  }
  book(start, end) {
    // check if the new event overlaps with any of the existing overlaps
    for (let i = 0; i < this.overlaps.length; i++) {
      let [s, e] = this.overlaps[i];
      if (start < e && end > s) return false;
    }
    // check if the new event overlaps with any of the existing events
    for (let i = 0; i < this.calendar.length; i++) {
      const [s, e] = this.calendar[i];
      if (start < e && end > s) {
        this.overlaps.push([Math.max(start, s), Math.min(end, e)]);
      }
    }
    this.calendar.push([start, end]);
    return true;
  }
}

const myCalendarTwo = new MyCalendarTwo2();
console.log(myCalendarTwo.book(10, 20)); // return True, The event can be booked.
console.log(myCalendarTwo.book(50, 60)); // return True, The event can be booked.
console.log(myCalendarTwo.book(10, 40)); // return True, The event can be double booked.
console.log(myCalendarTwo.book(5, 15)); // return False, The event cannot be booked, because it would result in a triple booking.
