#--- Day 11: Cosmic Expansion ---

grid=open("../testcase.txt").read().splitlines()

rows=len(grid)
cols=len(grid[0])

# Find the Empty row and col
empty_rows=[ r for r, row in enumerate(grid) if(row.count(".") == rows)]


empty_cols=[ c for c, col in enumerate(zip(*grid)) if(col.count(".")==cols) ]

# get the coordinates of our points

points=[(r,c) for r in range(rows) for c in range(cols) if grid[r][c]=="#"]



def CosmicExpansion():
    print("Cosmic Expansion Solution")

    print("Part 1: ", part1())
    print("Part 2: ", part2())

def distance(a,b,scale=2):
    r1,c1=a
    r2,c2=b

    #
    r1,r2=min(r1,r2),max(r1,r2)
    c1,c2=min(c1,c2),max(c1,c2)
    ans=0
    for r in range(r1,r2):
        ans+=scale if r in empty_rows else 1

    for c in range(c1,c2):
        ans+=scale if c in empty_cols else 1

    return ans

def part1():
    total=0
    scale=2

    for i ,(r1,c1) in enumerate(points):
        for (r2,c2) in points[:i]:
            d=distance((r1,c1),(r2,c2),scale)

            total+=d
    return total

def part2():
    total=0
    scale=1000000

    for i ,(r1,c1) in enumerate(points):
        for (r2,c2) in points[:i]:
            d=distance((r1,c1),(r2,c2),scale)

            total+=d
    return total

if __name__ == "__main__":
    CosmicExpansion()

