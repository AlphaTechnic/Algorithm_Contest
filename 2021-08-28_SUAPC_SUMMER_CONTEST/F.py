"""
input :
2
5 2
3 0

output :
48
12
"""
import sys

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        N, K = map(int, input().rstrip().split())
        s = max(1, N - K)
        e = N

        print(((s + e) * 2) * (e - s + 1))
