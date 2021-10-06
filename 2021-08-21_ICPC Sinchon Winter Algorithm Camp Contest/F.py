"""
input :
4 8
XFDFFFCX
ELFXLFFX
LFLXXLFX
DLFFFFLD

output :
31
"""
import sys
from collections import deque
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


def move_fun(cy, cx):
    while True:
        cy += 1
        if board[cy][cx] != 'X':
            return cy, cx


def bfs(caty, catx):
    global ey, ex
    que = deque()
    visited[caty][catx] = 0
    que.append((caty, catx, board[caty][catx]))

    while que:
        cy, cx, state = que.popleft()

        if (cy, cx) == (ey, ex):
            return

        if state == 'F' or state == 'C':
            for dy, dx in [(0, 1), (0, -1)]:
                ny, nx = cy + dy, cx + dx
                if not (0 <= ny < R and 0 <= nx < C): continue
                if board[ny][nx] == 'D': continue
                if visited[ny][nx] != -1: continue

                visited[ny][nx] = visited[cy][cx] + 1
                que.append((ny, nx, board[ny][nx]))

            for dy, dx in [(1, 0), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if not (0 <= ny < R and 0 <= nx < C): continue
                if board[ny][nx] != 'L': continue
                if visited[ny][nx] != -1: continue

                visited[ny][nx] = visited[cy][cx]
                que.append((ny, nx, board[ny][nx]))

        elif state == 'L':
            for dy, dx in [(1, 0), (-1, 0)]:
                ny, nx = cy + dy, cx + dx
                if not (0 <= ny < R and 0 <= nx < C): continue
                if board[ny][nx] == 'D': continue
                if visited[ny][nx] != -1: continue

                visited[ny][nx] = visited[cy][cx] + 5
                que.append((ny, nx, board[ny][nx]))

        elif state == 'X':
            ny, nx = move_fun(cy, cx)
            if not (0 <= ny < R and 0 <= nx < C): continue
            if board[ny][nx] == 'D': continue
            if visited[ny][nx] != -1: continue

            visited[ny][nx] = visited[cy][cx] + 10
            que.append((ny, nx, board[ny][nx]))


if __name__ == "__main__":
    R, C = map(int, input().rstrip().split())
    board = []
    for r in range(R):
        for c in range(C):
            board.append(list(input().rstrip()))

    caty = -1
    catx = -1
    ey = -1
    ex = -1
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'C':
                caty = r
                catx = c
            elif board[r][c] == 'E':
                ey = r
                ex = c

    visited = [[-1 for _ in range(C)] for _ in range(R)]
    bfs(caty, catx)

    print(visited)

    if visited[ey][ex] == -1:
        print("dodo sad")
    else:
        print(visited[ey][ex])

