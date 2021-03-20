import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

N = int(input())
mov = [(1, 0), (0, -1), (-1, 0), (0, 1)]
board = []
for i in range(N):
    board.append(list(input()))

pos = []
for cx in range(N):
    for cy in range(N):
        if board[cx][cy] == 'X':
            for dx, dy in mov:
                nx = cx
                ny = cy
                while True:
                    nx = nx + dx
                    ny = ny + dy
                    if not (0 <= nx < N and 0 <= ny < N and board[nx][ny] == '.'):
                        break
                    else:
                        pos.append((nx, ny))
# print(board)
cnt = dict(Counter(pos))
for i, j in pos:
    if cnt[(i, j)] >= 2:
        board[i][j] = 'B'

for i in range(N):
    for j in range(N):
        print(board[i][j], end='')
    print()
