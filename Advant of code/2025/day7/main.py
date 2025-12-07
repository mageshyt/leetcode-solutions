"""
Suddenly, you find yourself in an unfamiliar room! The room has no doors; the only way out is the teleporter. Unfortunately, the teleporter seems to be leaking magic smoke.

Since this is a teleporter lab, there are lots of spare parts, manuals, and diagnostic equipment lying around. After connecting one of the diagnostic tools, it helpfully displays error code 0H-N0, which apparently means that there's an issue with one of the tachyon manifolds.

You quickly locate a diagram of the tachyon manifold (your puzzle input). A tachyon beam enters the manifold at the location marked S; tachyon beams always move downward. Tachyon beams pass freely through empty space (.). However, if a tachyon beam encounters a splitter (^), the beam is stopped; instead, a new tachyon beam continues from the immediate left and from the immediate right of the splitter.
"""
# ===================== PART 1 =====================

def countBeamSplit(grid):
    rows,cols = len(grid), len(grid[0])
    beam_positions = set()
    splitters_hit = 0

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                beam_positions.add((row+1,col))


    while beam_positions:
        new_beam_position = set()

        for row , col in beam_positions:
            
            if row >= rows:
                continue

            currentCell = grid[row][col]
            print('[CURR,(row,col)]',currentCell,(row,col))
            if currentCell == '^':
                splitters_hit+=1
                if col-1 > 0:
                    new_beam_position.add((row+1 ,col-1))
                if col + 1 < cols-1:
                    new_beam_position.add((row+1 ,col+1))

            else:
                new_beam_position.add((row+1,col))
        beam_positions=new_beam_position
    return splitters_hit

# ===================== PART 2 =====================
"""
With your analysis of the manifold complete, you begin fixing the teleporter. However, as you open the side of the teleporter to replace the broken manifold, you are surprised to discover that it isn't a classical tachyon manifold - it's a quantum tachyon manifold.

With a quantum tachyon manifold, only a single tachyon particle is sent through the manifold. A tachyon particle takes both the left and right path of each splitter encountered.

Since this is impossible, the manual recommends the many-worlds interpretation of quantum tachyon splitting: each time a particle reaches a splitter, it's actually time itself which splits. In one timeline, the particle went left, and in the other timeline, the particle went right.

To fix the manifold, what you really need to know is the number of timelines active after a single particle completes all of its possible journeys through the manifold.

In the above example, there are many timelines. For instance, there's the timeline where the particle always went left:

.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
....|..........
...|^.^...^....
...|...........
..|^.^...^.^...
..|............
.|^...^.....^..
.|.............
|^.^.^.^.^...^.
|..............
Or, there's the timeline where the particle alternated going left and right at each splitter:

.......S.......
.......|.......
......|^.......
......|........
......^|^......
.......|.......
.....^|^.^.....
......|........
....^.^|..^....
.......|.......
...^.^.|.^.^...
.......|.......
..^...^|....^..
.......|.......
.^.^.^|^.^...^.
......|........
Or, there's the timeline where the particle ends up at the same point as the alternating timeline, but takes a totally different path to get there:

.......S.......
.......|.......
......|^.......
......|........
.....|^.^......
.....|.........
....|^.^.^.....
....|..........
....^|^...^....
.....|.........
...^.^|..^.^...
......|........
..^..|^.....^..
.....|.........
.^.^.^|^.^...^.
......|........
In this example, in total, the particle ends up on 40 different timelines.

Apply the many-worlds interpretation of quantum tachyon splitting to your manifold diagram. In total, how many different timelines would a single tachyon particle end up on?

"""
def countBeamSplit2(grid):
    rows,cols = len(grid), len(grid[0])
    beam_positions = set()
    total_timelines = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'S':
                beam_positions.add((row+1,col))
                break
    
    dp = {}
    def dfs(row, col):
        if row >= rows:
            return 1

        if (row,col) in dp:
            return dp[(row,col)]
        currentCell = grid[row][col]
        if currentCell == '^':
            left_paths = dfs(row+1, col-1) if col-1 >= 0 else 0
            right_paths = dfs(row+1, col+1) if col+1 < cols else 0
            dp[(row,col)] = left_paths + right_paths
            return left_paths + right_paths
        else:
            dp[(row,col)]=dfs(row+1, col)

            return dp[(row,col)]

    for row, col in beam_positions:
        total_timelines += dfs(row, col)
    return total_timelines



import os

os.chdir(os.path.dirname(__file__))
# read the input file
with open("input.txt", "r") as file:
    input_data = file.read().strip().split('\n')
    grid = [list(line) for line in input_data]
    print(countBeamSplit(grid))
    print(countBeamSplit2(grid))

