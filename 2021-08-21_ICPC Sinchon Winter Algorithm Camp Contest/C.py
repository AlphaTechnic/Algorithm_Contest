"""
input :
5
output :
3 2 4 5 1
"""
import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    nums = []
    for i in range(1, N + 1):
        nums.append(i)

    cut = N // 2
    for i in range(cut):
        print(nums[i], end=' ')
    for i in range(N - 1, cut - 1, -1):
        print(nums[i], end=' ')
