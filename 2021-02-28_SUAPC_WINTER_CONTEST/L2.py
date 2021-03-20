import sys
sys.stdin = open("input.txt", "r")


def restore(cy, cx, cnt):
    tmp_Rpos = []
    tmp = cnt
    for dx, dy in mov:
        nx, ny = cx, cy
        while True:
            nx, ny = nx + dx, ny + dy
            # 종료조건들
            if not 0 <= nx < N: break
            if not 0 <= ny < N: break
            if board[ny][nx] == 'R': break

            # 종료조건을 통과한다면,...
            if board[ny][nx] == 'X':
                board[ny][nx] = 'R'
                tmp_Rpos.append((ny, nx))
                tmp -= 1
                break
            elif board[ny][nx] == 'O':
                for ny, nx in tmp_Rpos:
                    board[ny][nx] = 'X'
                return cnt
    if cnt > tmp:
        B_pos.append((cy, cx))
    return tmp


N = int(input())
mov = [(1, 0), (0, -1), (-1, 0), (0, 1)]
board = []
for i in range(N):
    board.append(list(input()))

B_pos = []
X_pos = []
dot_pos = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 'X':
            X_pos.append((i, j))
        elif board[i][j] == '.':
            dot_pos.append((i, j))

set_dot_pos = set(dot_pos)
X_cnt = len(X_pos)
for i, j in set_dot_pos:
    X_cnt = restore(i, j, X_cnt)
    if X_cnt == 0: break


for i, j in B_pos:
    board[i][j] = 'B'
for i in range(N):
    for j in range(N):
        if board[i][j] == 'R':
            board[i][j] = 'X'
    print("".join(board[i]))

