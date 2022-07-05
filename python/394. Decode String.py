'''Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"'''


class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        curr_str='' # result string
        curr_num=0
        for char in s:
            if char =='[':
                stack.append(curr_str) # push current string to stack
                stack.append(curr_num) # push current number to stack
                curr_str='' # reset current string
                curr_num=0 # reset current number
            elif char ==']':
                repeat_num=stack.pop()
                prev_str=stack.pop()
                curr_str=prev_str+curr_str*repeat_num
            elif char.isdigit():
                curr_num=curr_num*10+int(char)
            else:
                curr_str+=char

        return  curr_str

if __name__ == "__main__":
    s=Solution()
    print(s.decodeString("3[a]2[bc]"))
    print(s.decodeString("3[a2[c]]"))

        