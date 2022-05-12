`Let’s simulate a game ‘Hot potato’. It is the game where children stand in a
circle and pass some objects to their neighbours. At a certain point in the game,
the action is stopped and the child who has the object is removed from the
circle. Play continues until only one child is left. Let’s simulate the scenario by
removing a child when the count becomes 7.
Our program will input a list of names and a constant, call it “num,” to be used
for counting. It will return the name of the last person remaining after repetitive
counting by num.
To simulate the circle, we will use a queue. Assume that the child at the front of
the queue says 1 and joins back the queue (dequeued and enqueued
immediately). The child at the front will say 2 and joins back the queue. This
repeats until a child says 7 (dequeued permanently). The game again starts from
count 1. This process will continue until only one name remains (the size of the
queue is 1)`;

const simulateHotPotato = (names, num) => {
  const queue = names;
  let c = 0;
  let length = num;
  while (length !== 1) {
    if (c !== 7) {
      queue.unshift(queue.pop());
      c++;
    } else {
      const p = queue.pop();
      console.log(p);
      c = 0;
      length--;
    }
  }
  return queue;
};

console.log(
  simulateHotPotato(["Bread", "Kent", "Jane", "susan", "David", "Bill"], 7)
);
