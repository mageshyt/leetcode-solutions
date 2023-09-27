"""
You are given an encoded string s. To decode the string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit d, the entire current tape is repeatedly written d - 1 more times in total.
Given an integer k, return the kth letter (1-indexed) in the decoded string.

 

Example 1:

Input: s = "leet2code3", k = 10
Output: "o"
Explanation: The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".
Example 2:

Input: s = "ha22", k = 5
Output: "h"
Explanation: The decoded string is "hahahaha".
The 5th letter is "h".
Example 3:

Input: s = "a2345678999999999999999", k = 1
Output: "a"
Explanation: The decoded string is "a" repeated 8301530446056247680 times.
The 1st letter is "a".

"""
class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        stack = []
        for i in s:
            if i.isalpha():
                stack.append(i)
            else:
                stack = stack*int(i)
            if len(stack) >= k:
                return stack[k-1]
            
        return ''
            
        #Time complexity: O(n)
        # Space complexity: O(n)           

    def decodeAtIndex2(self, s: str, k: int) -> str:
        size = 0  # Initialize a variable to keep track of the size of the encoded string
        for i in s:
            if i.isalpha():
                size += 1  # If character is a letter, increment the size
            else:
                size *= int(i)  # If character is a digit, multiply the size by that factor
        
        for i in reversed(s):
            k %= size  # Update k based on the size
            if k == 0 and i.isalpha():
                return i  # If k is 0 and the current character is a letter, return the character
            if i.isalpha():
                size -= 1  # If the character is a letter, decrement the size
            else:
                size /= int(i)  # If the character is a digit, divide the size by that factor
        
        return ''  # If k is out of bounds, return an empty string
        
        # Time complexity: O(n)
        # Space complexity: O(1)





print(Solution().decodeAtIndex2("y959q969u3hb22odq595",222280369))