class Solution:
    def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
        # Get the number of required skills and people
        n = len(req_skills)
        m = len(people)

        # Create a dictionary to map each skill to its index
        skillMap = {skill: i for i, skill in enumerate(req_skills)}

        # Create a dynamic programming table to store the result
        dp = [None] * (1 << n)
        dp[0] = []

        # Convert each person's skills to a bitmask representation
        skillPerson = []
        for i in range(m):
            val = 0
            for skill in people[i]:
                val |= 1 << skillMap[skill]
            skillPerson.append(val)

        # Identify banned pairs of people who have overlapping skills
        banned = [False] * m
        for i in range(m):
            for j in range(i + 1, m):
                val = skillPerson[i] | skillPerson[j]
                if val == skillPerson[i]:
                    banned[j] = True
                elif val == skillPerson[j]:
                    banned[i] = True

        # Perform dynamic programming to find the smallest sufficient team
        for i in range(m):
            if banned[i]:
                continue
            curSkill = skillPerson[i]

            for j in range(len(dp)):
                if dp[j] is None:
                    continue
                comb = j | curSkill
                if dp[comb] is None or len(dp[j]) + 1 < len(dp[comb]):
                    dp[comb] = dp[j] + [i]

        # Return the smallest sufficient team at the end of the dynamic programming process
        return dp[(1 << n) - 1]
