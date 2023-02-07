'''You are given a positive integer num. You may swap any two digits of num that have the same parity (i.e. both odd digits or both even digits).

Return the largest possible value of num after any number of swaps.

 

Example 1:

Input: num = 1234
Output: 3412
Explanation: Swap the digit 3 with the digit 1, this results in the number 3214.
Swap the digit 2 with the digit 4, this results in the number 3412.
Note that there may be other sequences of swaps but it can be shown that 3412 is the largest possible number.
Also note that we may not swap the digit 4 with the digit 1 since they are of different parities.
Example 2:

Input: num = 65875
Output: 87655
Explanation: Swap the digit 8 with the digit 6, this results in the number 85675.
Swap the first digit 5 with the digit 7, this results in the number 87655.
Note that there may be other sequences of swaps but it can be shown that 87655 is the largest possible number.
'''

import heapq


class Solution:
    def largestInteger(self, num: int) -> int:
        # covert to list
        list_num = [int(i) for i in str(num)]
        # get the even and odd list
        even_list = []
        odd_list = []

        for i in range(len(list_num)):
            if list_num[i] % 2 == 0:
                heapq.heappush(even_list, -list_num[i])
            else:
                heapq.heappush(odd_list, -list_num[i])

        # swap
        for i in range(len(list_num)):

            if list_num[i] % 2 == 0:
                # it will pop the largest even number
                list_num[i] = -heapq.heappop(even_list)
            else:
                # it will pop the largest odd number
                list_num[i] = -heapq.heappop(odd_list)

        return int(''.join([str(i) for i in list_num]))


if __name__ == '__main__':
    s = Solution()
    print(s.largestInteger(1234))
    print(s.largestInteger(65875))
