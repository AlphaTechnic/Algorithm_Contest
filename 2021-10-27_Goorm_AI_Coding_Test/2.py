"""
input :
3
popooqoq
bvdobvd
banana

output :
Mirror
Mirror
Normal
"""
import sys
from collections import defaultdict

sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

pair = defaultdict(str, {
    'b': 'd', 'd': 'b',
    'i': 'i',
    'l': 'l',
    'm': 'm',
    'n': 'n',
    'o': 'o',
    'p': 'q', 'q': 'p',
    's': 'z', 'z': 's',
    'u': 'u',
    'v': 'v',
    'w': 'w',
    'x': 'x',
})

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        txt = input().rstrip()
        L = len(txt)

        for i in range(L // 2 + 1):
            if txt[i] != pair[txt[L - 1 - i]]:
                print("Normal")
                break
        else:
            print("Mirror")
