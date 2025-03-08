"""
You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', representing the color of the ith block. The characters 'W' and 'B' denote the colors white and black, respectively.

You are also given an integer k, which is the desired number of consecutive black blocks.

In one operation, you can recolor a white block such that it becomes a black block.

Return the minimum number of operations needed such that there is at least one occurrence of k consecutive black blocks.

 

Example 1:

Input: blocks = "WBBWWBBWBW", k = 7
Output: 3
Explanation:
One way to achieve 7 consecutive black blocks is to recolor the 0th, 3rd, and 4th blocks
so that blocks = "BBBBBBBWBW". 
It can be shown that there is no way to achieve 7 consecutive black blocks in less than 3 operations.
Therefore, we return 3.

"""
class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        start=0
        min_recolor=float('inf')
        white_count=0

        for end in range(len(blocks)):
            window_size=end-start+1
            if blocks[end]=='W':
                white_count+=1

            if window_size>=k:
                min_recolor=min(min_recolor,white_count)
                if blocks[start]=='W':
                    white_count-=1
                start+=1

        return min_recolor

# Time complexity is O(n)
# Space complexity

print(Solution().minimumRecolors("WBBWWBBWBW",7)) #3
print(Solution().minimumRecolors("WWWWWWWWWW",7)) #0


