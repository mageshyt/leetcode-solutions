"""An undirected graph of n nodes is defined by edgeList, where edgeList[i] = [ui, vi, disi] denotes an edge between nodes ui and vi with distance disi. Note that there may be multiple edges between two nodes.

Given an array queries, where queries[j] = [pj, qj, limitj], your task is to determine for each queries[j] whether there is a path between pj and qj such that each edge on the path has a distance strictly less than limitj .

Return a boolean array answer, where answer.length == queries.length and the jth value of answer is true if there is a path for queries[j] is true, and false otherwise.

 

Example 1:


Input: n = 3, edgeList = [[0,1,2],[1,2,4],[2,0,8],[1,0,16]], queries = [[0,1,2],[0,2,5]]
Output: [false,true]
Explanation: The above figure shows the given graph. Note that there are two overlapping edges between 0 and 1 with distances 2 and 16.
For the first query, between 0 and 1 there is no path where each distance is less than 2, thus we return false for this query.
For the second query, there is a path (0 -> 1 -> 2) of two edges with distances less than 5, thus we return true for this query.
Example 2:


Input: n = 5, edgeList = [[0,1,10],[1,2,5],[2,3,9],[3,4,13]], queries = [[0,4,14],[1,4,13]]
Output: [true,false]
Explanation : The above figure shows the given graph."""


class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList, queries):

        UF = {}

        def find(x):
            UF.setdefault(x, x)
            print("UF", UF)
            if x != UF[x]:
                print("setting UF[x] to find(UF[x])")
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            print("find(x),find(y)", find(x), find(y))
            UF[find(x)] = find(y)

        # edgeList -> [u,v,dis]
        # queries -> [p,q,limit]

        # sort the edgeList

        edgeList.sort(key=lambda x: x[2])  # sort by distance

        # add idx to queries

        queries = [(p, q, limit, idx)
                   for idx, (p, q, limit) in enumerate(queries)]

        # sort the queries by limit
        queries.sort(key=lambda x: x[2])

        print(edgeList, queries)

        res = [False]*len(queries)

        # for each query, we check the edgeList and add the edge
        # to the union find if the distance is smaller than the limit
        i = 0
        for p, q, limit, idx in queries:
            # edgeList[i][2] is the distance
            while i < len(edgeList) and edgeList[i][2] < limit:
                u, v, dis = edgeList[i]
                union(u, v)
                i += 1

            if find(p) == find(q):
                res[idx] = True
        print(UF)
        return res

    # TLE
    #    Time complexity : O((n+q)log(n+q))  where n is the number of edges, and q is the number of queries.
    #    Space complexity : O(n+q)


# class Solution:
if __name__ == "__main__":
    s = Solution()
    print(s.distanceLimitedPathsExist(
        3, [[0, 1, 2], [1, 2, 4], [2, 0, 8], [1, 0, 16]], [[0, 1, 2], [0, 2, 5]]))
    # print(s.distanceLimitedPathsExist(
    #     5, [[0, 1, 10], [1, 2, 5], [2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13]]))
    # print(s.distanceLimitedPathsExist(5, [[0, 1, 10], [1, 2, 5], [
    #       2, 3, 9], [3, 4, 13]], [[0, 4, 14], [1, 4, 13], [2, 4, 13]]))
