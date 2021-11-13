# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import defaultdict

ele2num = defaultdict(int)


def solution(arr):
    # write your code in Python 3.6
    # 원소의 개수를 헤아린다.
    for ele in arr:
        ele2num[ele] += 1

    tot = 0
    for ele in ele2num:
        # case 1. 숫자를 아예 사라지게 만들기
        case1 = ele2num[ele]

        # case 2. 수 X의 갯수를 X개로 맞추기
        case2 = abs(ele - ele2num[ele])
        tot += min(case1, case2)

    return tot


if __name__ == "__main__":
    print(solution([1, 2, 2, 2, 5, 5, 5, 8]))
