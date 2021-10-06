"""
input :
4 5
c.xc
....
xx..
...x
x..x

output :
1
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

C, R = map(int, input().split())
board = []
for _ in range(R):
    board.append(list(input().rstrip()))

for r in range(R):
    for c in range(C):
        print(board[r][c], end='')
    print()

