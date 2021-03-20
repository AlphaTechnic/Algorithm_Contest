"""
input :
3 5
3 4 5
2 3 9
3 9 3
4 5 1
1 3 6
output :
33
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

C, R = map(int, input().split())
dp = []
for _ in range(R):
    dp.append(list(map(int, input().split())))

for c in range(1, C):
    dp[0][c] += dp[0][c-1]
for r in range(1, R):
    dp[r][0] += dp[r-1][0]

for r in range(1, R):
    for c in range(1, C):
        dp[r][c] = dp[r][c] + max(dp[r-1][c], dp[r][c-1])

print(dp[R-1][C-1])