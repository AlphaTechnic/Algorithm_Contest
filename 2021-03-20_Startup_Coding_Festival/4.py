"""
input :
4.0 3.0 2.1 4.3 5.0
2 3
WYO
YYO
ABC
DCE

output :
D 4.3 1 0
B 3.0 0 1
C 2.1 1 1
E 5.0 1 2
C 2.1 0 2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
tmp_list = list(map(float, input().rstrip().split()))
prefer = dict()

ascii = 65
for preference in tmp_list:
    prefer[chr(ascii)] = preference
    ascii += 1

R, C = map(int, input().split())
info = []
genre = []
for _ in range(R):
    info.append(list(input().rstrip()))
for _ in range(R):
    genre.append(list(input().rstrip()))

W_pos = []
Y_pos = []
O_pos = []
for r in range(R):
    for c in range(C):
        if info[r][c] == 'W':
            W_pos.append([prefer[genre[r][c]], genre[r][c], r, c])
        elif info[r][c] == 'Y':
            Y_pos.append([prefer[genre[r][c]], genre[r][c], r, c])
        else:
            O_pos.append([prefer[genre[r][c]], genre[r][c], r, c])

Y_pos.sort(reverse=True, key=lambda x: (x[0], -x[2], -x[3]))
for component in Y_pos:
    print(component[1], component[0], component[2], component[3])
O_pos.sort(reverse=True, key=lambda x: (x[0], -x[2], -x[3]))
for component in O_pos:
    print(component[1], component[0], component[2], component[3])

print(Y_pos)