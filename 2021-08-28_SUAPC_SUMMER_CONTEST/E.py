"""
input :
2 2
az

output :

"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline
alpha2num = dict()

if __name__ == "__main__":
    N, M = map(int, input().rstrip().split())
    S = input().rstrip()

    for i in range(97, 123):
        alpha2num[chr(i)] = i - 97
    print(alpha2num)

    tot = 1
    for ch in S:
        if alpha2num[ch] + M + 1 <= 25:
            tot *= M + 1
        else:
            tot *= alpha2num['z'] - alpha2num[ch] + 1
    print(tot)