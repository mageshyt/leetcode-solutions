"""
You have a bomb to defuse, and your time is running out! Your informer will provide you with a circular array code of length of n and a key k.

To decrypt the code, you must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, return the decrypted code to defuse the bomb!


"""


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n
        
        res = [0] * n
        window_sum = 0

        # if k is positive

        if k > 0:
            # lets find the first window sum
            for i in range(1, k+1):
                window_sum += code[i]

            for i in range(n):
                res[i] = window_sum

                # update window sum

                window_sum -= code[(i+1) % n]
                window_sum += code[(i+k+1) % n] # next element


        # if k is negative
        else:
            # lets find the first window sum
            for i in range(n+k, n):
                window_sum += code[i]

            for i in range(n):
                res[i] = window_sum

                # update window sum

                window_sum -= code[(i+n+k) % n]
                window_sum += code[i] # previous element



        return res

# Time: O(n) | Space: O(n)

