
"""
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:
    
"""


directions = [(-1, -1), (-1, 0), (-1, 1),
      (0, -1),           (0, 1),
      (1, -1), (1, 0), (1, 1)]

# ========================= PART 1 =========================
from typing import List, Tuple

def count_xmas(grid: List[List[str]]) -> int:
    rows, cols = len(grid), len(grid[0])
    # directions = [(0, 1), (1, 0), (1, 1), (1, -1), (0, -1), (-1, 0), (-1, -1), (-1, 1)]
    target_word = "XMAS"
    count = 0

    def backtrack(row: int, col: int, index: int, direction: Tuple[int, int]) -> bool:
        # Out of bounds or character mismatch
        if not (0 <= row < rows and 0 <= col < cols) or grid[row][col] != target_word[index]:
            return False
        # If the entire word is found
        if index == len(target_word) - 1:
            return True

        # Move in the given direction
        new_row, new_col = row + direction[0], col + direction[1]
        return backtrack(new_row, new_col, index + 1, direction)

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == target_word[0]:  # Starting character match
                for direction in directions:
                    if backtrack(i, j, 0, direction):
                        count += 1

    return count

# ========================= PART 2 =========================


import sys

if sys.argv[1]=="test":
    test_ip=open("./testcase.txt","r").read().split('\n')
else:
    test_ip=open("./input.txt","r").read().strip().split('\n')

wordGrid=[
    list(s) for s in test_ip if len(s)>0
]

print(count_xmas(wordGrid))
