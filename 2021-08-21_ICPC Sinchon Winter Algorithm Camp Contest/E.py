"""
input :
5 5
1 2
1 3
2 3
3 4
4 5

output :
3 2
1 2 3
1 2
4 5
5
"""
import sys
from collections import deque
sys.setrecursionlimit(10 ** 6)
sys.stdin = open("input.txt")
input = sys.stdin.readline


def find(x):
    if parent[x] == -1:
        return x
    parent[x] = find(parent[x])
    return parent[x]


def union(a, b):
    a = find(a)
    b = find(b)
    if a == b:
        return False

    if height[a] < height[b]:
        a, b = b, a
    parent[b] = a

    if height[a] == height[b]:
        height[a] += 1

    return True


def bfs(s):
    nds = []
    edges = []

    que = deque()
    visited[s] = True
    que.append(s)
    nds.append(s)


    while que:
        cur = que.popleft()
        for nxt in range(1, V + 1):
            if MST_mat[cur][nxt] == 0: continue
            if visited[nxt]: continue

            visited[nxt] = True
            que.append(nxt)
            nds.append(nxt)
            edges.append(nxt)
    return nds, edges


if __name__ == "__main__":
    V, E = map(int, input().rstrip().split())
    if V == 1:
        print(-1)
        exit()

    parent = [-1 for _ in range(V + 1)]
    height = [0 for _ in range(V + 1)]

    edges = []
    for i in range(1, E + 1):
        a, b = map(int, input().rstrip().split())
        edges.append((a, b, i))

    to_del = set()
    MST_mat = [[0 for _ in range(V + 1)] for _ in range(V + 1)]
    for a, b, name in edges:
        if union(a, b):
            MST_mat[a][b] = name
            MST_mat[b][a] = name
        else:
            to_del.add((a, b, name))

    flag = False
    for a in range(1, V + 1):
        for b in range(1, V + 1):
            if MST_mat[a][b] != 0:
                MST_mat[a][b] = 0
                MST_mat[b][a] = 0
                flag = True
                break
        if flag:
            break

    visited = [False for _ in range(V + 1)]
    for i in range(1, V + 1):
        for j in range(i, V + 1):
            if visited[i]: continue

            nds, edges = bfs(i)
            for nd in nds:
                print(nd, end=' ')
            print()
            for edge in edges:
                print(edge, end=' ')
            print()
