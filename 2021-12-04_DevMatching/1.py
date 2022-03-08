def chk(bd, R, C, c):
    star_cnt = 0

    r = 0
    while True:
        if bd[r][c] == '#':
            r += 1
        elif bd[r][c] == '>':
            c += 1
            if c >= C:
                return False
        elif bd[r][c] == '<':
            c -= 1
            if c < 0:
                return False
        elif bd[r][c] == '*':
            if star_cnt == 0:
                r += 1
                star_cnt += 1
            elif star_cnt == 1:
                return False

        if r >= R:
            return True


def solution(drum):
    bd = drum
    R = len(drum)
    C = len(drum[0])

    cnt = 0
    for c in range(C):
        if chk(bd, R, C, c):
            cnt += 1
    return cnt


if __name__ == "__main__":
    drum = ["######", ">#*###", "####*#", "#<#>>#", ">#*#*<", "######"]
    solution(drum)
