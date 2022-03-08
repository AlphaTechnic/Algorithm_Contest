DIR = ((-1, 1), (0, 1), (1, 1), (1, 0))


def chk(cy, cx, n, direction, board):
    R = len(board)
    C = len(board[0])

    dy, dx = DIR[direction]
    ny, nx = cy, cx
    for _ in range(n):
        if not (0 <= ny < R and 0 <= nx < C):
            return 0
        if board[ny][nx] != '1':
            return 0
        ny, nx = ny + dy, nx + dx

    # (n + 1)목 방지
    y1, x1 = cy - dy, cx - dx
    if (0 <= y1 < R and 0 <= x1 < C) and board[y1][x1] == '1':
        return 0
    y2, x2 = ny, nx
    if (0 <= y2 < R and 0 <= x2 < C) and board[y2][x2] == '1':
        return 0

    return 1


def solution(h, w, n, board):
    tot = 0
    for i in range(h):
        for j in range(w):
            for direction in range(4):
                res = chk(i, j, n, direction, board)
                # if res != 0:
                # print(i, j, direction)
                tot += res
    return tot


print(solution(7, 9, 4, ["111100000", "000010011", "111100011", "111110011", "111100011", "111100010", "111100000"]))
print(solution(5, 5, 5, ["11111", "11111", "11111", "11111", "11111", ]))
