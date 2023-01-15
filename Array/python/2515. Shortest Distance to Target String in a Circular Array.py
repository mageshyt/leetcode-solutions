'''You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

 

Example 1:

Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.
Example 2:

Input: words = ["a","b","leetcode"], target = "leetcode", startIndex = 0
Output: 1
Explanation: We start from index 0 and can reach "leetcode" by
- moving 2 units to the right to reach index 3.
- moving 1 unit to the left to reach index 3.
The shortest distance to reach "leetcode" is 1.
Example 3:

Input: words = ["i","eat","leetcode"], target = "ate", startIndex = 0
Output: -1
Explanation: Since "ate" does not exist in words, we return -1.'''



class Solution:
    def closetTarget(self, words, target: str, startIndex: int)  :
        min_distance=float('inf')

        for i in range(len(words)):
            if words[i]==target:
                diff=abs(i-startIndex) # n
                diff2=len(words)-diff # n -x for another direction
                min_distance=min(min_distance,diff,diff2)

        

        if min_distance==float('inf'):
            return -1
        return min_distance 


if __name__ == "__main__":
    s=Solution()
    print(s.closetTarget(["hello","i","am","leetcode","hello"],"hello",1))
    print(s.closetTarget(["a","b","leetcode"],"leetcode",0))
    print(s.closetTarget(["i","eat","leetcode"],"ate",0))


 