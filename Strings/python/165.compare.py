from itertools import zip_longest
from traceback import print_tb
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        # now lets split the version 
        splitted_version1 = version1.split('.')
        splitted_version2 = version2.split('.')
        # now lets find max length of the two versions
        max_length = max(len(splitted_version1), len(splitted_version2))
        for i in range(max_length):
            curr_v_1=0
            curr_v_2=0
            if (i < len(splitted_version1)):
                curr_v_1=int(splitted_version1[i])
            if (i < len(splitted_version2)):
                curr_v_2=int(splitted_version2[i])
      
            
            if (curr_v_1 > curr_v_2): return 1
            if (curr_v_1 < curr_v_2): return -1 
        return 0


testCase1=Solution()
print(testCase1.compareVersion("1.01.04", "1.01"))