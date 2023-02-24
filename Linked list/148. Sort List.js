`Given the head of a linked list, return the list after sorting it in ascending order.

 

Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []`;

const sortList = (head) => {
  if (!head || !head.next) return head;
  //! now lets split the Linked list
  let right = GetMid(head);
  let left = head;
  let temp = right.next;
  right.next = null;
  right = temp;
  //! now lets sort the left and right
  left = MergeSort(left);
  right = MergeSort(right);

  const GetMid = (head) => {
    let slow = head;
    let fast = head;
    while (fast.next && fast.next.next) {
      slow = slow.next;
      fast = fast.next.next;
    }
    return slow;
  };


  const MergeSort = (list_1, list_2) => {
    let dummy = new ListNode();
    let tail = new ListNode();
    while (list_1 && list_2) {
      if (list_1.val < list_2.val) {
        tail.next = list_1;
        list_1 = list_1.next;
      } else {
        tail.next = list_2;
        list_2 = list_2.next;
      }
      tail = tail.next;
    }
    if (list_1) tail.next = list_1;
    if (list_2) tail.next = list_2;
    return dummy.next;
  };


  
  //! now lets merge the left and right
  return Merge(left, right);
};
