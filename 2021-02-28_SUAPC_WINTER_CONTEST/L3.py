import sys
sys.stdin = open("input.txt", "r")

pos = []

N = int(input())
mov = [(1, 0), (0, -1), (-1, 0), (0, 1)]
board = []
for i in range(N):
    board.append(list(input()))
chk = [0 for _ in range(N)]

for cy in range(N):
    for cx in range(N):
        if board[cy][cx] == 'X':
            ny = cy
            nx = cx
            for dy, dx in mov:
                ny = cy + dy
                nx = cx + dx
                if not (0<= ny <N and 0<= nx <N):
                    continue



