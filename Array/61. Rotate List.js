`Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:

`;
const reverse_list = (head, left, right) => {
  let prev = null;
  let curr = head;
  while (curr != null && left < right) {
    const temp = curr.next;
    curr.next = prev;
    prev = head;
    curr = temp;
    left++;
    right;
  }
  return prev;
};
const rotateRight = (head, k) => {
  // Edge Case
  if (!head || k == 0) return head;
  // ! let us make tail has head
  let tail = head;
  let count = 1;
  while (tail.next) {
    tail = tail.next;
    count++;
  }
  tail.next = head; // ! we will be in the last node and we make last node next has head
  `
    Example 1:
        1-->2-->3-->4-->5
        after looping
        tail = 5
        tail.next will be 5-->1-->2-->3-->4
  `;
  let curr = head;

  for (let i = 0; i < count - (k % count) - 1; i++) {
    curr = curr.next;
  }
  ans = curr.next;
  curr.next = null;
  return ans;
};
