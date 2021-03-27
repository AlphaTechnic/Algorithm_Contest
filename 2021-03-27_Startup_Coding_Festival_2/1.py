"""
input :
7 00:05:48
02:14
03:34
02:34
03:45
05:43
01:34
02:33
output :
2 1
"""

import sys
sys.stdin = open("input.txt", "r")
input = sys.stdin.readline

N, tmp = input().split()
N = int(N)
tmp = list(map(int, tmp.split(':')))
T = tmp[0] * 3600 + tmp[1] * 60 + tmp[2]

play_times = []
play_times_accumulated = []
for i in range(N):
    tmp_list = list(map(int, input().split(':')))
    t = tmp_list[0] * 60 + tmp_list[1]
    if i == 0:
        play_times.append(t)
        play_times_accumulated.append(t)
    else:
        play_times.append(t)
        play_times_accumulated.append(play_times_accumulated[-1] + t)

play_times = [0] + play_times
play_times_accumulated = [0] + play_times_accumulated

if play_times_accumulated[0] > T:
    print(1, 1)
    exit()

max_val = 0
start = 0
for i in range(N):
    for j in range(i, N):
        if play_times_accumulated[j] - play_times_accumulated[i] >= T:
            if j-i > max_val:
                max_val = j-i
                start = i
            break
print(max_val, start + 1)