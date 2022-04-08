Please dont downvote guys if cannot support,We are putting lot of effort in it🙂



What the Question asking us to do 🤔 ?
The Question is asking us to add the value and return the kth largest element in the array.

What we going to do ✅ ?
1.We are going to use minHeap
2.in minHeap we can add and pop the element in log(n) time which is more optimized
3.we can get min value at O(1)
4.our heap should be k size because we are need to return kth largest element
Example:
example our heap=[3,4,5,8] k=3 so k th largest element is 4 and we no need 3 so will pop it and make our head=[4,5,8] which is length == k

Solution Explanation:
Inputs:
arr=[4,5,8,2]
k=3
now we are going to make heap
heap=[2,4,5,8]
now we are going to pop the element which is 2 and make our heap=[4,5,8] because we need only k sized heap
Big o:
n-->size of the s
Time: O((n-k)log n) k could be small so O(n logn)
Space: O(n)


UPVOTE if you like 😃 , If you have any question, feel free to ask.

