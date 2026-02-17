"""
A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

For example, the below binary watch reads "4:51".


Given an integer turnedOn which represents the number of LEDs that are currently on (ignoring the PM), return all possible times the watch could represent. You may return the answer in any order.

The hour must not contain a leading zero.

For example, "01:00" is not valid. It should be "1:00".
The minute must consist of two digits and may contain a leading zero.

For example, "10:2" is not valid. It should be "10:02".
 

Example 1:

Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

"""

from typing import List
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        hours = [1,2,4,8] # 4 bits
        minutes = [1,2,4,8,16,32] # 6 bits

        def backtrack(turnedOn ,hour, minute, idx):
            if turnedOn == 0:
                if hour < 12 and minute < 60:
                    res.append(f"{hour}:{minute:02d}")
                return
            
            for i in range(idx, len(hours) + len(minutes)):
                if i < len(hours):
                    backtrack(turnedOn - 1, hour + hours[i], minute, i + 1)
                else:
                    backtrack(turnedOn - 1, hour, minute + minutes[i - len(hours)], i + 1)

        res = []
        backtrack(turnedOn, 0, 0, 0)

        return res

if __name__ == "__main__":
    turnedOn = 1
    print(Solution().readBinaryWatch(turnedOn)) # Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

