# --- Day 16: The Floor Will Be Lava ---

# (.) -> pass through
# (/ \) -> mirror reflect 90
# (|) -> splitter (go up and down)
# (-) -> splitter (go left and right)

from collections import deque 

grid=open("../testcase.txt").read().splitlines()

def FloorLava():
    print("Part 1 Resulst >>",part1())
    print("Part 2 Resulst >>",part2())


def helper(row,col,dr,dc):
    # row,col,dr,dc 
    a=[(row,col,dr,dc)]
    seen=set()
    q=deque(a)

    while q:
        row,col,dr,dc=q.popleft()
        row+=dr
        col+=dc

        if row <0 or row>=len(grid) or col <0 or col>=len(grid[0]):
            continue

        curr=grid[row][col]
        # print(">>",curr)
        # if empyt then pass, and horz splitter and moving alone col then pass and vert splitter move alone row then pass
        if curr=="." or (curr=="-" and dc!=0) or (curr=="|" and dr!=0):
            if (row,col,dr,dc) not  in seen:
                seen.add((row,col,dr,dc))
                q.append((row,col,dr,dc))
        
        elif curr=='/':
            # flip them if going right then go down 
            # (0,1)=> (-1,0) r->d
            # (1,0)=>(0,-1) l->up
            # (-1,0) => (0,1) d->r
            # (1,0) => (1,0) up->l
            # dr,dc=> -dc,-dr
            dr,dc= -dc,-dr

            if (row,col,dr,dc) not in seen:
                q.append((row,col,dr,dc))
                seen.add((row,col,dr,dc))
        elif curr=="\\":
            dr,dc= dc,dr

            if (row,col,dr,dc) not in seen:
                q.append((row,col,dr,dc))
                seen.add((row,col,dr,dc))
        else:
            for dr,dc in [(1,0),(-1,0)] if curr=="|" else [(0,1),(0,-1)]:
                if (row,col,dr,dc) not in seen:
                    seen.add((row,col,dr,dc))
                    q.append((row,col,dr,dc))

    coords={(r,c) for (r,c,_,_) in seen}
    return len(coords)

def part1():
   
    return helper(0,-1,0,1)

def part2():
    max_val=0
    for r in range(len(grid)):
        max_val=max(max_val,helper(r,-1,0,1))
        max_val=max(max_val,helper(r,len(grid[0]),0,-1))
    return max_val



FloorLava()
