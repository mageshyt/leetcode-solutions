Hello guys 😀 !

Given question:
Given an array of integers nums which is *** sorted in ascending order ***,
an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.


Question Explanation:
    basically, we need to check if the target is in the array. using binary search.


Explanation:
    lets declare a variable called left and right.
    left = 0
    right = len(nums) - 1


Big O:
    n--> number of elements in the array
    Time Complexity: O(log(n)) - because we are using binary search
    Space Complexity: O(1)