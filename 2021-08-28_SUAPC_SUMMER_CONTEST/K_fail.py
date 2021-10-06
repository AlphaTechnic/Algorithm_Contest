"""
input :
3 2
4 3
1 3
7 4
5 2
8 3

output :
2
"""

import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    M, N = map(int, input().rstrip().split())
    Q = list()
    B = list()
    for _ in range(M):
        a, b = map(int, input().rstrip().split())
        Q.append((a, b))
    for _ in range(N):
        a, b = map(int, input().rstrip().split())
        B.append((a, b))

    Qcpy = [Q[i] for i in range(len(Q))]
    Bcpy = [B[i] for i in range(len(B))]

    Q.sort(key=lambda x: (-x[0], x[1]))
    B.sort(key=lambda x: (-x[0], x[1]))
    Qcpy.sort(key=lambda x: (x[1], -x[0]))
    Bcpy.sort(key=lambda x: (x[1], -x[0]))

    ind1 = 0
    ind2 = 0
    cnt1 = 0
    while True:
        q_sz, q_time = Q[ind1]
        b_sz, b_time = B[ind2]
        if q_sz <= b_sz:
            if q_time >= b_time:
                cnt1 += 1
                ind1 += 1
                ind2 += 1
            else:
                ind1 += 1
        else:
            ind1 += 1

        if ind1 == len(Q) or ind2 == len(B):
            break

    ind1 = 0
    ind2 = 0
    cnt2 = 0
    while True:
        q_sz, q_time = Q[ind1]
        b_sz, b_time = Bcpy[ind2]
        if q_sz <= b_sz:
            if q_time >= b_time:
                cnt2 += 1
                ind1 += 1
                ind2 += 1
            else:
                ind1 += 1
        else:
            ind1 += 1

        if ind1 == len(Q) or ind2 == len(Bcpy):
            break
    print(max(cnt1, cnt2))