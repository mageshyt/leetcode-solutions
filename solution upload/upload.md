**Please dont downvote guys if cannot support,We are putting lot of effort in it🙂**

```What the Question asking us to do 🤔 ?

    Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    Approach Explanation :
        1. we will create  hashmap to count the frequency of the number
        2. we will create a new array to store the k most frequent elements
        3. we will find the frequency of the number and store it in the hashmap
        4. we will iterate through the hashmap and store the k most frequent elements in the new array
        5. we will return the new array

Big o:
    n-->size of the nums
    Time: O(n)
    Space: O(n+n) --> O(n)

```

`Javascript`

```
const topKFrequent = (nums, k) => {
  const map = new Map(); //! map to count the frequency of the number
  for (let num of nums) {
    map.set(num, map.get(num) + 1 || 1);
  }
  const result = [];
  for (let [key, value] of map) {
    result.push([key, value]); //! we will add the number and its frequency
  }
  result.sort((a, b) => b[1] - a[1]); //! we will solve with respect to the frequency of the number
  return result.slice(0, k).map((x) => x[0]); //! we will slice the list with respect to length of k
};
```



`UPVOTE if you like 😃 , If you have any question, feel free to ask.`
