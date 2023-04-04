class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        count = 0

        for i in range(len(startTime)):
            st = startTime[i]
            et = endTime[i]

            if st <= queryTime <= et:
                count += 1

        return count
