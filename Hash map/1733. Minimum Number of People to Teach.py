"""
On a social network consisting of m users and some friendships between users, two users can communicate with each other if they know a common language.

You are given an integer n, an array languages, and an array friendships where:

There are n languages numbered 1 through n,
languages[i] is the set of languages the ihuser knows, and
You can choose one language and teach it to some users so that all friends can communicate with each other. Return the minimum number of users you need to teach.

Note that friendships are not transitive, meaning if x is a friend of y and y is a friend of z, this doesn't guarantee that x is a friend of z.
 

Example 1:

Input: n = 2, languages = [[1],[2],[1,2]], friendships = [[1,2],[1,3],[2,3]]
Output: 1
Explanation: You can either teach user 1 the second language or user 2 the first language.
Example 2:

Input: n = 3, languages = [[2],[1,3],[1,2],[3]], friendships = [[1,4],[1,2],[3,4],[2,3]]
Output: 2
Explanation: Teach the third language to users 1 and 3, yielding two users to teach.
 


"""

from typing import List
class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        lang_map = {}
        for i, langs in enumerate(languages):
            lang_map[i + 1] = set(langs)
        
        cannot_communicate = set()
        for u, v in friendships:
            if lang_map[u].intersection(lang_map[v]):
                continue
            # if they cannot communicate, add them to the set
            cannot_communicate.add(u)
            cannot_communicate.add(v)
        
        # if everyone can communicate, return 0
        if not cannot_communicate:
            return 0
        
        lang_count = [0] * (n + 1)
        for user in cannot_communicate:
            for lang in lang_map[user]:
                lang_count[lang] += 1
        # return the minimum number of users to teach
        return len(cannot_communicate) - max(lang_count)

print(Solution().minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]])) # 1
