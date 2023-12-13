#--- Day 13: Point of Incidence ---


# (.) ash
# (#) rock

with open("../testcase.txt") as f:
    pattern=[lines.split("\n") for lines in f.read().strip().split("\n\n")]


print(len(pattern))

# method to transpose the matrix

def transpose(matrix):
    return list(zip(*matrix))


def is_horizontal_symmetry(grid, row_index):
 
    num_rows, num_cols = len(grid), len(grid[0])

    # Iterate through each column in the grid
    for col_index in range(num_cols):
        # Iterate through each row on one side of the specified row
        for relative_row_index in range(num_rows):
            # Calculate the symmetric row index on the opposite side of the specified row
            symmetric_row_index = (row_index * 2 + 1) - relative_row_index

            # Check if the symmetric row index is within valid row indices
            if not (0 <= symmetric_row_index < num_rows):
                continue

            # Compare the element at the current row and column with its symmetric counterpart
            if grid[relative_row_index][col_index] != grid[symmetric_row_index][col_index]:
                # If any pair of elements are not equal, the row is not horizontally symmetric
                return False

    # If all comparisons pass, the row exhibits horizontal symmetry
    return True


def pointOfIncidence():
    print("Point of Incidence Solution")

    ans=0
    for grid in pattern:
        print("??")
        ans+=part1(grid)

    print("Part 1: ", ans)

    print("Part 2: ", part2())


def part1(grid):
    n, m = len(grid), len(grid[0])

    horiz = -1
    for i in range(n-1):
        if is_horizontal_symmetry(grid, i):
            horiz = i
            break

    vert = -1
    T = transpose(grid)
    for j in range(m-1):
        if is_horizontal_symmetry(T, j):
            vert = j
            break

    assert vert == -1 or horiz == -1
    return vert + 1 + 100 * (horiz + 1)


def part2():
    pass

pointOfIncidence()