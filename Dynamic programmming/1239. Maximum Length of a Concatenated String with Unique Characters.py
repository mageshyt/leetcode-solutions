from typing import List
from collections import defaultdict


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        cache = defaultdict(int)

        def dfs(word,  prev, i):
            if (word, prev, i) in cache:
                return cache[(word, prev, i)]

            if i >= len(arr):
                return len(word)
            print(">>", word, i, prev)

            for idx, w in enumerate(arr):
                if prev != w:
                    # check it words contain any letter in the word
                    flag = False
                    for c in w:
                        if c in word:
                            flag = True
                            break
                    if not flag:
                        cache[(word, prev, i)] = max(
                            dfs(word+w,  w, idx), cache[(word, prev, i)])

            return cache[(word, prev, i)]

        dfs("",  "", 0)
        print(cache)


print(Solution().maxLength(["un", "iq", "ue"]))
