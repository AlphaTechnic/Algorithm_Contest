import sys
sys.stdin = open("input.txt", "r")
sys.setrecursionlimit(1000000)


N, root = map(int, input().split())
graph = [[] for _ in range(N+2)]
for _ in range(N-1):
    a, b, w = map(int, input().split())
    graph[a].append((b, w))
    graph[b].append((a, w))

print(graph)

visited = [False for _ in range(N+1)]
pillar_len = 0
if len(graph[root]) == 1:
    visited[root] = True
    for nxt, w in graph[root]:
        if visited[nxt] == False:
            root = nxt
            pillar_len += w
    while len(graph[root]) == 2:
        for nxt_node, weight in graph[root]:
            if visited[nxt_node] == False:
                pillar_len += weight
                visited[root] = True
                root = nxt_node

giga_root = root
print("giga_root : ", giga_root)
print(pillar_len, end=' ')

visited = [False for _ in range(N+1)]
ans = 0
tmp = 0


def get_max_length(root):
    global tmp
    global ans
    if graph[root] == []:
        if tmp > ans:
            ans = tmp
        return ans

    for nxt, weight in graph[root]:
        tmp += weight
        get_max_length(nxt)
        tmp -= weight


get_max_length(root)
print(ans)

