"""
input :
10 11 12

output :
4
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline


if __name__ == "__main__":
    N = int(input())
    M = input()
    K = int(input())
    M = M[-K - 1:]

    if '1' in M:
        print("NO")
    else:
        print("YES")

