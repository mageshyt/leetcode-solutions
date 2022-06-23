'''There are n different online courses numbered from 1 to n. You are given an array courses where courses[i] = [durationi, lastDayi] indicate that the ith course should be taken continuously for durationi days and must be finished before or on lastDayi.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.

 

Example 1:

Input: courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
Output: 3
Explanation: 
There are totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
Example 2:

Input: courses = [[1,2]]
Output: 1
Example 3:

Input: courses = [[3,2],[4,3]]
Output: 0'''


from calendar import c
import heapq


class Solution:
    def scheduleCourse(self, courses) -> int:
      courses.sort(key=lambda x: x[1]) # sort the courses by last_day

      curr_time=0
      history_heap=[]

      for duration , last_day in courses:
        if curr_time+duration<=last_day: # if the course can be taken in this time slot then add it to the heap
          heapq.heappush(history_heap,-duration)
          curr_time+=duration

        else:
           if history_heap: # to make sure our heap is not empty
            longes_course=-history_heap[0] # get the longest course in heap first will be longest value
            if longes_course > duration:
              heapq.heappop(history_heap) # remove the longest course from heap
              heapq.heappush(history_heap,-duration) # add the new course to the heap
              curr_time+=duration-longes_course # update the curr_time
      print(history_heap)
      return len(history_heap)



if __name__ == '__main__':
    courses = [[100,200],[200,1300],[1000,1250],[2000,3200]]
    s = Solution()
    print(s.scheduleCourse(courses))

          