"""
input :
6 6
6 4
6 5
4 1
4 2
4 3
1 4
4 1
6 5
1 6
6 3
4 3

output :
no
yes
yes
no
yes
yes
"""

import sys
sys.setrecursionlimit(5000)
sys.stdin = open("input.txt", "r")


def is_parent(a, b):
    while b != parent[b]:
        if b == a:
            return True
        b = parent[b]
    if b == a:
        return True
    return False


def union_parent(a, b):
    parent[b] = a


V, Q = map(int, input().split())
parent = [i for i in range(V + 1)]
childs = []

for _ in range(V - 1):
    a, b = map(int, input().split())
    union_parent(a, b)



print(parent)
for _ in range(Q):
    a, b = map(int, input().split())
    if is_parent(a, b):
        print("yes")
    else:
        print("no")
