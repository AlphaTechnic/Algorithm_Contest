"""
input :
3
12:00 ~ 23:59
11:00 ~ 18:00
14:00 ~ 20:00
"""
import sys
import re

sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N = int(input())
tmp_list = []
for _ in range(N):
    parsing = re.split('[:~ ]+', input().rstrip())
    s = parsing[0] + parsing[1]
    e = parsing[2] + parsing[3]
    tmp_list.append([s, e])

start = max(tmp_list, key=lambda x: x[0])[0]
end = min(tmp_list, key=lambda x: x[1])[1]

if start <= end:
    print(str(start)[0:2] + ':' + str(start)[2:] + ' ~ ' + str(end)[0:2] + ':' + str(end)[2:])
else:
    print(-1)
