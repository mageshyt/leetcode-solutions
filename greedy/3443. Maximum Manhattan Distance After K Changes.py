class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        x, y = 0, 0
        distances = []

        for move in s:
            if move == "N":
                y += 1
            elif move == "S":
                y -= 1
            elif move == "E":
                x += 1
            elif move == "W":
                x -= 1
            distances.append(abs(x) + abs(y))

        if len(distances) == 1 or k == 0:
            return max(distances)

        max_dist = distances[1]
        previous = distances[0]
        added_boost = 0

        for i in range(1, len(distances)):
            if distances[i] < previous and k > 0:
                added_boost += 2
                k -= 1
            previous = distances[i]
            distances[i] += added_boost
            max_dist = max(max_dist, distances[i])

        return max_dist
