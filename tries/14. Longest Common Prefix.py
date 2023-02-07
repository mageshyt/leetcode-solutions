'''Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
'''
class Solution:
    def longestCommonPrefix(self, strs) -> str:

        longest = ""
        if len(strs) == 0:
            return longest


        words= strs
        count = 0

        while True:
            try:
                letter = words[0][count]
            except:
                break
            for word in words:
                try:
                    if word[count] != letter:
                        return longest
                except:
                    return longest
            longest += letter
            count += 1


            

        return longest



if __name__ == '__main__':

    print(Solution().longestCommonPrefix(["flower","flow","flight"]))


