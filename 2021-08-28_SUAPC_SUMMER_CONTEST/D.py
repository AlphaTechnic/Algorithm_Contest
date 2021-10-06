"""
input :
3
0.30 0.40 0.50

output :
2.16
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    pp = list(map(float, input().rstrip().split()))

    if N == 1:
        print(pp[0])
        exit()

    tot = 0
    ind = 0
    while True:
        tot += pp[ind]
        tot += (pp[ind] * (1 - pp[ind + 1])) + ((1 - pp[ind]) * pp[ind + 1])

        if ind + 1 == len(pp) - 1:
            tot += pp[ind + 1]
            break
        ind += 1
    print(tot)
