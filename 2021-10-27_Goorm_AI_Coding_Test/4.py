"""
input :
3
Hello, World!
I'm your father.
What are you doing here?

output :
eoo
Iouae
aaeouoiee
"""
import sys
sys.stdin = open("input.txt", 'r')
input = sys.stdin.readline

chk = {'a', 'e', 'i', 'o', 'u'
       'A', 'E', 'I', 'O', 'U'}

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        txt = input().rstrip()

        flag = False
        for i in range(len(txt)):
            if txt[i] in chk:
                flag = True
                print(txt[i], end='')
        if not flag:
            print("???", end='')
        print()

