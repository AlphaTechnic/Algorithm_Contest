import sys
import collections
sys.stdin = open("input.txt", "r")

input = sys.stdin.readline
N, M = map(int, input().split())
words = []
for i in range(N):
    word = input().rstrip()
    if len(word) >= M:
        words.append(word)

cnt = collections.Counter(words)
words.sort(key=lambda x: (-cnt[x], -len(x), str(x)))
words = list(collections.OrderedDict.fromkeys(words).keys())
for i in words:
    print(i)