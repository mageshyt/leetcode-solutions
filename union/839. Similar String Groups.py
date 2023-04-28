"""Two strings X and Y are similar if we can swap two letters (in different positions) of X, so that it equals Y. Also two strings X and Y are similar if they are equal.

For example, "tars" and "rats" are similar (swapping at positions 0 and 2), and "rats" and "arts" are similar, but "star" is not similar to "tars", "rats", or "arts".

Together, these form two connected groups by similarity: {"tars", "rats", "arts"} and {"star"}.  Notice that "tars" and "arts" are in the same group even though they are not similar.  Formally, each group is such that a word is in the group if and only if it is similar to at least one other word in the group.

We are given a list strs of strings where every string in strs is an anagram of every other string in strs. How many groups are there?

 

Example 1:

Input: strs = ["tars","rats","arts","star"]
Output: 2
Example 2:

Input: strs = ["omv","ovm"]
Output: 1"""

class Solution:
    def numSimilarGroups(self, strs) -> int:

        groups=0

        vis={} # visited map

        for i in range(len(strs)):
            if i not in vis:
                groups+=1

                self.dfs(i,strs,vis)
        print(vis)
        return groups
        
        
    
    def dfs(self,start:int,strs,vis):
        # mark visited as true
        vis[start]=True
        for j in range(len(strs)):
            # if already visited then continue
            if(j in vis):continue

            if (self.is_similar(strs[start],strs[j])):
                self.dfs(j,strs,vis)

    def is_similar(self,str1,str2):
        count=0

        for i in range(len(str1)):
            # if exceed our limit 
            if count >3:
                return False

            if (str1[i] != str2[i]):
                count+=1
                pass
        # we can have at most 2 changed or no changes 
        # no changes -> both are equal
        return count==2 or count==0


if __name__ == "__main__":
    strs = ["tars","rats","arts","star"]
    s=Solution()
    print(s.numSimilarGroups(strs))




