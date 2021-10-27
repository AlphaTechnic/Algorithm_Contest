"""
input :
100 100
4

output :
131 69
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

if __name__ == "__main__":
    a, b = map(int, input().rstrip().split())
    N = int(input())

    p = 0
    while p != N:
        if p % 2 == 0:
            if a % 2 == 0:
                a, b = a - a // 2, b + a // 2
            else:
                a, b = a - (a // 2 + 1), b + (a // 2 + 1)
        else:
            if b % 2 == 0:
                a, b = a + b // 2, b - b // 2
            else:
                a, b = a + (b // 2 + 1), b - (b // 2 + 1)
        p += 1
    print(a, b)
