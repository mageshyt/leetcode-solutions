
from typing import List

class TrieNode:
    def __init__(self):
        self.children= {}
        self.isEnd= False

class Trie:
    def __init__(self, words):
        self.root= TrieNode()
        for word in words:
            self.insert(word)



    def insert(self, word):
        node= self.root
        for char in word:
            if char not in node.children:
                node.children[char]= TrieNode()
            node= node.children[char]
        node.isEnd= True

    def search(self, word):
        node= self.root
        for char in word:
            if char not in node.children:
                return False
            node= node.children[char]
        return node.isEnd

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        # remove duplicate words
        words= set(dictionary)
        memo= {}
        trie= Trie(words).root

        def dfs(start):
            # base case
            if start == len(s):
                return 0
            if start in memo:
                return memo[start]

            # default case : skip the current character
            result= dfs(start+1) + 1
            curr= trie


            # check if the current character is the start of a words
            for i in range(start,len(s)):
                char=s[i]
                # we can find a word can form from the current character
                if char not in curr.children:
                    break
                curr= curr.children[char]

                if curr.isEnd:
                    result= min(result, dfs(i+1))



            memo[start]= result
            return result
        return dfs(0)

# Time complexity: O(n^2)
# Space complexity: O(n)

print(Solution().minExtraChar("ab", ["a", "b"])) # 0
print(Solution().minExtraChar("leetscode", ["leet", "code", "leetcode"])) # 0

     
