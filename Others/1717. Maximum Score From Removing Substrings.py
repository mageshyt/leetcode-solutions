
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:

        def calculate_score(pair,score):
            nonlocal s
            res=0
            stack=[]
            for char in s:
                # if the current character is the second character of the pair
                if stack and stack[-1]==pair[0] and char==pair[1]:
                    res+=score
                    stack.pop()
                else:

                    stack.append(char)
            # update the string
            s="".join(stack)

            return res

        res=0

        pair="ab" if x>y else "ba"
        # calculate the score for the first pair
        res+=calculate_score(pair,max(x,y))
        # calculate the score for the second pair
        res+=calculate_score(pair[::-1],min(x,y))

        return res


# Time complexity: O(n)
# Space complexity: O(n)

print(Solution().maximumGain("cdbcbbaaabab", 4, 5)) # 19