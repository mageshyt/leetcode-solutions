'''Problem
Statement

Noor is going fish farming. There are N types of fish. Each type of fish has size(S) and eating factor(E). A fish with eating factor of E, will eat all the fish of size .

Help Noor to select a set of fish such that the size of the set is maximized as well as they do not eat each other.


Input

The first line contains T, the number of test cases. The first line of a test case contains an integers N. N is the number of types of fish. Each of the next N lines contains two integers S and E meaning the size and eating factor of a fish.

Output

For each test cases, print a single integer, the maximum number of fish Noor can have in his pond. 


'''
def solution():
    T = int(input())
    for _ in range(T):
        N = int(input())
        fish = []
        for _ in range(N):
            S, E = map(int, input().split())
            fish.append((S, E))
        fish.sort(key=lambda x: x[1])
        size = 0
solution()
    
