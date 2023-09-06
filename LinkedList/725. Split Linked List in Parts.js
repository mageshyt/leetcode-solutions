`Given the head of a singly linked list and an integer k, split the linked list into k consecutive linked list parts.

The length of each part should be as equal as possible: no two parts should have a size differing by more than one. This may lead to some parts being null.

The parts should be in the order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal to parts occurring later.

Return an array of the k parts.

 

Example 1:


Input: head = [1,2,3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but its string representation as a ListNode is [].
`;

// Define a function to compute the length of a linked list
const computeLength = (head) => {
  let count = 0;
  while (head) {
    count++;
    head = head.next;
  }
  return count;
};

// Define a function to split a linked list into 'k' parts
const splitListToParts = (head, k) => {
    // Time Complexity: O(N + k) where N is the length of the linked list
    // Space Complexity: O(k)

  const result = []; // Initialize an array to store the resulting linked list parts
  // Compute the length of the input linked list
  const length = computeLength(head);

  // Compute the base size and the number of extra elements
  let base_size = Math.floor(length / k);
  let extra = length % k;

  let curr = head; // Initialize a pointer to the head of the linked list

  for (let i = 0; i < k; i++) {
    // Push the current part to the result array
    result.push(curr);

    let size = base_size + (extra > 0 ? 1 : 0); // Compute the size of the current part

    for (let j = 0; j < size - 1; j++) {
      if (curr) curr = curr.next; // Move the pointer to the next element if available
      else break; // Break if the end of the linked list is reached
    }

    if (curr) {
      let temp = curr.next; // Store the next node in a temporary variable
      curr.next = null; // Set the next pointer of the current node to null
      curr = temp; // Move the current pointer to the next node
    }

    extra--; // Decrement the extra count
  }

  return result; // Return the array containing the linked list parts
};
