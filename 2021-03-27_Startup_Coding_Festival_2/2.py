"""
input :
6
seoul beijing 3
beijing hawaii 10
seoul tokyo 4
seoul hawaii 6
tokyo hawaii 5
beijing tokyo 5

output :
12
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def find_parent(x):
    if x == parent[x]:
        return parent[x]
    parent[x] = find_parent(parent[x])
    return parent[x]


def union_parent(a, b):
    A = find_parent(a)
    B = find_parent(b)
    if A < B:
        parent[B] = A
    else:
        parent[A] = B


E = int(input())
edges = []
parent = [i for i in range(2*E)]
hash_table = dict()

cnt = 1
for _ in range(E):
    a, b, cost = input().split()
    cost = int(cost)
    if a not in hash_table:
        hash_table[a] = cnt
        cnt += 1
    if b not in hash_table:
        hash_table[b] = cnt
        cnt += 1
    edges.append((cost, hash_table[a], hash_table[b]))
    edges.append((cost, hash_table[b], hash_table[a]))


edges.sort()
total = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        total += cost

print(total)

a = {1, 2}
b = {3, 4}
print(type(a))
print(a+b)

