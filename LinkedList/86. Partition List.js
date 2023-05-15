`Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]
`;

const partition = (head, x) => {
  let left = new ListNode(0); // this node will have all the nodes less than x
  let right = new ListNode(0); // this node will have all the nodes greater than or equal to x
  let lessTail = left;
  let greaterTail = right;
  while (head) {
    // ! if current head val is less than x, add it to the left list
    const currval = head.val;
    if (currval < x) {
      lessTail.next = head;
      lessTail = lessTail.next;
    } else {
      // ! if current head val is greater than or equal to x, add it to the right list
      greaterTail.next = head;
      greaterTail = greaterTail.next;
    }
    // ! move to next node
    head = head.next;
  }
  //! we are connecting the last node of the left list to the first node of the right list
  lessTail.next = right.next;
  greaterTail.next = null;
  //! we will point tail of left to null
  return left.next;
};
