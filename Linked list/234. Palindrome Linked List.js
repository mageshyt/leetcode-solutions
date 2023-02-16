`Given the head of a singly linked list, return true if it is a 
palindrome
 or false otherwise.

 

Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false`;

const isPalindrome = (head) => {
  const arr = [];
  while (head) {
    arr.push(head.val);
    head = head.next;
  }

  let left = 0;
  let right = arr.length - 1;

  while (left < right) {
    if (arr[left] !== arr[right]) return false;
    left++; // move left pointer to the right
    right--; // move right pointer to the left
  }

  return true;
};
