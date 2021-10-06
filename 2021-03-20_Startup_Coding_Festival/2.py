"""
input :
4
1101
output :
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
dp = ['_'] + list(map(int, list(input().rstrip())))

for ind, element in enumerate(dp):
    if ind == 0:
        pre = element
    else:
        if pre == 0 and element == 0:
            print(0)
            exit()
        else:
            pre = element

for i in range(3, N+1):
    if dp[i] == 0:
        continue
    dp[i] = dp[i-2] + dp[i-1]

print(dp[N])
