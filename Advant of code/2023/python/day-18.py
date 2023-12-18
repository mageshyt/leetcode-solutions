#--- Day 18: Lavaduct Lagoon ---

# Initialize starting point at the origin (0, 0)
points = [(0, 0)]

# Define movement directions as vectors
dirs = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}

# Initialize a variable to keep track of the total units moved
total_units_moved = 0

# Read the input file
lines= open("../testcase.txt").read().splitlines()


for line in lines:
    direction,units,_= line.split()
    # Convert units to int
    units = int(units)

    dr,dc= dirs[direction]
    # update unit moved
    total_units_moved += units

    # calculate the new points

    pre_row,pre_col = points[-1]

    new_points=(pre_row+dr*units,pre_col+dc*units)

    points.append(new_points)
# Calculate the signed area of the polygon using the shoelace formula

signed_area = abs(sum(
    points[i][0] * (points[i - 1][1] - points[(i + 1) % len(points)][1])
    for i in range(len(points))
)) // 2

centroid_index = signed_area - total_units_moved // 2 + 1

# Print the final result, which is the sum of the centroid index and total units moved
final_result = centroid_index + total_units_moved
print(final_result)
