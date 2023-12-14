# Read lines from the file
lines = open('../testcase.txt').read().splitlines()

grid=list(map("".join,zip(*lines)))


# Process each row to sort characters within '#' groups and join them with '#'
processed_rows = []
for row in grid:
    groups = ["".join(sorted(list(group), reverse=True)) for group in row.split("#")]
    processed_rows.append("#".join(groups))

# Transpose the processed rows to get columns
grid=list(map("".join,zip(*processed_rows)))


result=0



for r,row in enumerate(grid):
    result+=row.count("O") * (len(grid) -r)

print(result)