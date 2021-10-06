import sys
from collections import Counter
sys.stdin = open("input.txt", "r")

N = int(input())
nums = list(map(int, input().split()))
print(Counter(nums).most_common(1)[0][1])