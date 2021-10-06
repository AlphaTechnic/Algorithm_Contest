import sys
import math

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, K = map(int, input().split())
v = list(map(int, input().split()))
v.sort()

V = 0
m = v[0]
for x in range(1, N):
    V = max(V, m * x + v[x] * (N - x))

if K % V == 0:
    print(K // V)
else:
    print(K // V + 1)