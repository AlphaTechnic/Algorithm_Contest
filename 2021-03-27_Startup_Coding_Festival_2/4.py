"""
input :
5
dijkstra
greedy
bfs
backtracking
dynamic
3
bfs
greedyalgorithm
ra

output :
1
0
2
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

word_list = []
N = int(input())
for _ in range(N):
    word_list.append(input().rstrip())

#print(word_list)
Q = int(input())
patterns = []
for _ in range(Q):
    patterns.append(input().rstrip())

#print(patterns)
for pattern in patterns:
    cnt = 0
    for word in word_list:
        if pattern in word:
            cnt += 1
    print(cnt)