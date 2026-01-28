"""
Their plan is to connect the junction boxes with long strings of lights. Most of the junction boxes don't provide electricity; however, when two junction boxes are connected by a string of lights, electricity can pass between those two junction boxes.

The Elves are trying to figure out which junction boxes to connect so that electricity can reach every junction box. They even have a list of all of the junction boxes' positions in 3D space (your puzzle input).
This list describes the position of 20 junction boxes, one per line. Each position is given as X,Y,Z coordinates. So, the first junction box in the list is at X=162, Y=817, Z=812.

To save on string lights, the Elves would like to focus on connecting pairs of junction boxes that are as close together as possible according to straight-line distance. In this example, the two junction boxes which are closest together are 162,817,812 and 425,690,689.

By connecting these two junction boxes together, because electricity can flow between them, they become part of the same circuit. After connecting them, there is a single circuit which contains two junction boxes, and the remaining 18 junction boxes remain in their own individual circuits.


"""
from collections import defaultdict


class UnionFind:
    
    def __init__(self) -> None:
        self.UF = {}
 
    def find(self, x):
        self.UF.setdefault(x, x)
        if x != self.UF[x]:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]
    
    def union(self, x, y):
        self.UF[self.find(x)] = self.find(y)  # Merge two sets by making y's parent as x's parent

# ===================== PART 1 =====================
def euclidean_distance(coord1, coord2):
    return ((coord1[0] - coord2[0]) ** 2 + 
            (coord1[1] - coord2[1]) ** 2 + 
            (coord1[2] - coord2[2]) ** 2) ** 0.5
def countConnection(coordinates):
    uf = UnionFind()
    n = len(coordinates) # number of junction boxes

    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((dist, i, j))

    edges.sort()

    for k in range(min(1000,len(edges))):
        dist, u, v = edges[k]
        uf.union(u, v)

    components = defaultdict(int)

    for i in range(n):
        root = uf.find(i)
        components[root] += 1


    # sort components by size
    sorted_components = sorted(components.values(), reverse=True)

    return sorted_components[0]*sorted_components[1] *sorted_components[2]
# ===================== PART 2 =====================
"""
he Elves were right; they definitely don't have enough extension cables. You'll need to keep connecting junction boxes together until they're all in one large circuit.

Continuing the above example, the first connection which causes all of the junction boxes to form a single circuit is between the junction boxes at 216,146,977 and 117,168,530. The Elves need to know how far those junction boxes are from the wall so they can pick the right extension cable; multiplying the X coordinates of those two junction boxes (216 and 117) produces 25272.

Continue connecting the closest unconnected pairs of junction boxes together until they're all in the same circuit. What do you get if you multiply together the X coordinates of the last two junction boxes you need to connect?

"""

def multiplyLastConnection(coordinates):
    uf = UnionFind()

    noOfComponents = len(coordinates)
    n = len(coordinates) # number of junction boxes
    last_u, last_v = -1, -1

    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = euclidean_distance(coordinates[i], coordinates[j])
            edges.append((dist, i, j))


    for (dist,u ,v ) in sorted(edges):
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            noOfComponents -= 1
            last_u, last_v = u, v
            if noOfComponents == 1:
                break

    print(coordinates[last_u], coordinates[last_v])
    return coordinates[last_u][0] * coordinates[last_v][0]



import os

os.chdir(os.path.dirname(__file__))
# read the input file
with open("input.txt", "r") as file:
    input_data = file.read().strip().split('\n')
    coordinates = [tuple(map(int,line.split(','))) for line in input_data]

result = countConnection(coordinates)
print("Number of connected components:", result)

result2 = multiplyLastConnection(coordinates)
print("Product of X coordinates of last connected junction boxes:", result2)

