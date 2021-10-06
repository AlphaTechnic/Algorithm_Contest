"""
input :
4
1110
1110
0110
0000

output :
total: 11
size[1]: 8
size[2]: 3
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    board.append(list(map(int, input().rstrip())))

pos_1 = []
cnt = 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            pos_1.append((r, c))
            cnt += 1


def how_many_space(size):
    delta = size - 1
    count = 0
    for r, c in pos_1:
        escape = 0
        last_r, last_c = r + delta, c + delta
        if not 0 <= last_r < N: continue
        if not 0 <= last_c < N: continue
        for i in range(r, last_r + 1):
            for j in range(c, last_c + 1):
                if board[i][j] != 1:
                    escape = 1
                    break
            if escape == 1:
                break
        else:
            count += 1
    return count


res = ['_']
total = 0

for sz in range(1, N + 1):
    cnt_by_sz = how_many_space(sz)
    if cnt_by_sz == 0:
        break
    res.append(cnt_by_sz)
    total += cnt_by_sz
print('total:', total)
for ind, cnt in enumerate(res):
    if ind == 0:
        continue
    print('size[%s]:' % ind, cnt)
