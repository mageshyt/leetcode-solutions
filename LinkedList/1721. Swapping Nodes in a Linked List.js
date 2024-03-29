`You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping 
the values of the kth node from the beginning and the kth 
node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
`;

const swapNodes = (head, k) => {
  const tracker = new ListNode(0, head);
  const backTrack = new ListNode(0, head);
  while (k !== 0) {
    tracker = tracker.next;
    k--;
  }
  let temp_tracker = tracker;
  while (tracker.next !== null) {
    backTrack = backTrack.next;
    tracker = tracker.next;
  }
  [temp_tracker.val, backTrack.val] = [backTrack.val, temp_tracker.val];
  return head;
};
