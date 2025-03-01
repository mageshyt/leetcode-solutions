
def bfsTraversal():
    visited = set()
    queue = []
    queue.append(0)
    visited.add(0)

    while queue:
        vertex = queue.pop(0)
        print(vertex, end=" ")

        for i in graph[vertex]:
            if i not in visited:
                queue.append(i)
                visited.add(i)


def dfsTraversal():
    visited = set()
    stack = []
    stack.append(0)
    visited.add(0)

    while stack:
        vertex = stack.pop()
        print(vertex, end=" ")

        for i in graph[vertex]:
            if i not in visited:
                stack.append(i)
                visited.add(i)


graph = [[1, 2], [0, 3, 4], [0, 5], [1], [1], [2]]
bfsTraversal()
print()

dfsTraversal()
print()
