# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def get_grp(txt, i):
    cnt = 0
    p = txt[i]

    for i in range(i, len(txt) + 1):
        if i == len(txt):
            break

        if p == txt[i]:
            cnt += 1
        else:
            break
    return i, cnt


def solution(txt):
    # write your code in Python 3.6
    idx = 0
    mx_leng = 0
    lengs = []

    while idx < len(txt):
        idx, leng = get_grp(txt, idx)

        # max length의 길이를 업데이트
        mx_leng = max(mx_leng, leng)

        lengs.append(leng)

    # 가장 긴 길이와의 차이를 누적하여 return
    tot = 0
    for leng in lengs:
        tot += (mx_leng - leng)

    return tot


if __name__ == "__main__":
    print(solution("aaaab"))
