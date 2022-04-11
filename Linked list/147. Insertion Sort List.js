`Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:

Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list and inserts it there.
It repeats until no input elements remain.
The following is a graphical example of the insertion sort algorithm. The partially sorted list (black) initially contains only the first element in the list. One element (red) is removed from the input data and inserted in-place into the sorted list with each iteration.


 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]`;

const insertionSortList = (head) => {
  if (!head || !head.next) return head;
  let dummy = new ListNode(0, head);
  let curr = head.next;
  let prev = head;
  while (!!curr) {
    const curr_val = curr.val;
    const prev_val = prev.val;
    if (curr_val >= prev_val) {
      prev = curr;
      curr = curr.next;
      continue;
    }
    let temp = dummy;
    while (temp.next.val < curr_val) {
      temp = temp.next;
    }
    prev.next = curr.next;
    curr.next = temp.next;
    temp.next = curr;
    curr = prev.next;

  }
    return dummy.next;
};

// const insertionSortList = (nums) => {
//   for (let i = 1; i < nums.length; i++) {
//     let j = i - 1;
//     let current = nums[i];
//     while (j >= 0 && current < nums[j]) {
//       nums[j + 1] = nums[j];
//       j--;
//     }
//     nums[j + 1] = current;

//     console.log(nums);
//   }
//   return nums;
// };
// console.log(insertionSortList([5, 3, 6, 1, 12]));
