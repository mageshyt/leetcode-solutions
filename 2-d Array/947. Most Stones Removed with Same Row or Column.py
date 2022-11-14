from collections import defaultdict
from itertools import chain


class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:

        rows, cols = defaultdict(list), defaultdict(list)
        for s, (r, c) in enumerate(stones):  # and within the same column
            rows[r].append(s)  # belong to the same connected
            cols[c].append(s)  # let's store this data

        seen, n = set(), len(stones)

        def dfs(s):
            if s in seen:
                return 0  # connected component of each stone by
            seen.add(s)  # making recursive calls to adjacent
            r, c = stones[s]  # stones; it returns 1/0 depending on
            for ss in chain(rows[r], cols[c]):
                dfs(ss)  # whether the component was already
            return 1  # explored, thus, allowing to count them

        c = sum(dfs(s) for s in range(n))

        return n - c
