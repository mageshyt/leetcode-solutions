"""You are given an array of unique integers salary where salary[i] is the salary of the ith employee.

Return the average salary of employees excluding the minimum and maximum salary. Answers within 10-5 of the actual answer will be accepted.

 

Example 1:

Input: salary = [4000,3000,1000,2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively.
Average salary excluding minimum and maximum salary is (2000+3000) / 2 = 2500
Example 2:

Input: salary = [1000,2000,3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively.
Average salary excluding minimum and maximum salary is (2000) / 1 = 2000"""


class Solution:
    def average(self, salary) -> float:
        min_sal = min(salary)
        max_sal = max(salary)

        total = sum(salary)
        return (total-min_sal-max_sal)/(len(salary)-2)


if __name__ == '__main__':
    salary = [4000, 3000, 1000, 2000]
    instance = Solution()
    solution = instance.average(salary)
    print(solution)
