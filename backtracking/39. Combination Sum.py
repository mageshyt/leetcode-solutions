class Solution:
    def combinationSum(self, candidates, target: int):

        res = []

        def dfs(candidates, target, path, root):

            if target == 0:
                res.append(path)
                return

            if target < 0:
                return

            for i in range(len(candidates)):
                new_target = target - candidates[i]
                if new_target >= 0:
                    dfs(candidates[i:], new_target, path+[candidates[i]], i)

        dfs(candidates, target, [], 0)

        return res


if __name__ == "__main__":

    candidates = [2, 3, 6, 7]
    target = 7
    print(Solution().combinationSum(candidates, target))
