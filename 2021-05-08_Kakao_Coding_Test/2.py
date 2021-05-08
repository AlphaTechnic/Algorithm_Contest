attach = ((1, 0), (0, 1), (-1, 0), (0, -1))
check_point = {
    (1, 1): ((1, 0), (0, 1)),
    (1, -1): ((1, 0), (0, -1)),
    (-1, 1): ((-1, 0), (0, 1)),
    (-1, -1): ((-1, 0), (0, -1)),
    (2, 0): ((1, 0),),
    (-2, 0): ((-1, 0),),
    (0, 2): ((0, 1),),
    (0, -2): ((0, -1),),
}


def check(place):
    place = [list(string) for string in place]
    for x in range(5):
        for y in range(5):
            if place[x][y] == "P":
                for dx, dy in attach:
                    cx, cy = x + dx, y + dy
                    if not 0 <= cx < 5: continue
                    if not 0 <= cy < 5: continue
                    if place[cx][cy] == "P":
                        return 0
                for dx, dy in check_point:
                    cx, cy = x + dx, y + dy
                    if not 0 <= cx < 5: continue
                    if not 0 <= cy < 5: continue
                    if place[cx][cy] == "P":
                        barrier = True
                        for ddx, ddy in check_point[(dx, dy)]:
                            ccx, ccy = x + ddx, y + ddy
                            if place[ccx][ccy] == "O":
                                barrier = False
                        if barrier is False:
                            return 0
    return 1


def solution(places):
    res = []
    for place in places:
        res.append(check(place))
    return res


if __name__ == "__main__":
    places = [
        ["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
        ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
        ["OOOOO", "OOOOO", "PXPOO", "XPXOO", "OOOOO"],
    ]
    print(solution(places))
