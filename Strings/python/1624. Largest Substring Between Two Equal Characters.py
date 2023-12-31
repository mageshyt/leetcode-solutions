
from typing import List
from collections import defaultdict
class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        res=-1
        hash_map=defaultdict(list)
        for i in range(len(s)):
            hash_map[s[i]].append(i)
        for key in hash_map:
            if len(hash_map[key])>1:
                left_most=hash_map[key][0]
                right_most=hash_map[key][-1]
                res=max(res,right_most-left_most-1)

        return res