

def splitNum(num):
    nums = [int(i) for i in str(num)]

    pow = len(nums)-1

    res = []

    for i in nums:
        res.append(i*10**pow)
        pow -= 1

    return res


class Solution:
    def multiply(self, num1: str, num2: str) -> str:

        if num1 == "0" or num2 == "0":
            return "0"

        num1 = splitNum(num1)
        num2 = splitNum(num2)

 
        return str(sum([x*y for x in num1 for y in num2]))


if __name__ == "__main__":

    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1, num2))
