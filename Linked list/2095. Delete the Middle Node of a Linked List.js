const findLength = (head) => {
  let count = 0;
  let curr = head;
  while (curr) {
    count++;
    curr = curr.next;
  }
  return count;
};

const deleteMiddle = (root) => {
  if (!root.next) return null;
  let dummy1 = new ListNode(0, root);
  let dummy2 = new ListNode(0, dummy1);
  let rabbit = dummy2;
  let turtle = dummy2;
  while (rabbit.next && rabbit) {
    rabbit = rabbit.next.next;
    turtle = turtle.next;
  }
  turtle.next = turtle.next.next;
  return dummy1.next;
};
