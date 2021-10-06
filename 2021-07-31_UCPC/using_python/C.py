"""
input :
1 50 50

output :
1.6250000
"""
import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline


if __name__ == "__main__":
    SCALE, d, k = map(int, input().rstrip().split())
    d = d / 100
    k = k / 100

    CNT = 10 ** 6
    p = [0, d]
    for i in range(2, 10 ** 6):
        p.append(min(p[i - 1] * (1 + k), 1))
        if p[i] == 1:
            CNT = i
            break
    #print(p)

    q = [0 for _ in range(CNT + 1)]
    q[1] = 1 - d
    for i in range(2, CNT):
        q[i] = 1 - p[i]
    #print(q)

    q_accumul = [1]
    tot = 1
    for i in range(1, CNT + 1):
        tot *= q[i]
        q_accumul.append(tot)
    #print(q_accumul)

    tot = 0
    for i in range(1, CNT + 1):
        a = q_accumul[i - 1]
        b = p[i]
        c = SCALE * i
        tot += a * b * c

    print(tot)
