from collections import defaultdict
from datetime import datetime
from datetime import timedelta

date2value = defaultdict(int)


def solution(purchase):
    date = datetime.strptime("2019/01/01", "%Y/%m/%d")
    date2value[date] = 0
    while date != datetime.strptime("2019/12/31", "%Y/%m/%d"):
        date += timedelta(days=1)
        date2value[date] = 0

    for info in purchase:
        date_str, price = info.split()
        date = datetime.strptime(date_str, "%Y/%m/%d")
        for _ in range(30):
            date2value[date] += int(price)
            date += timedelta(days=1)

    br = 0
    si = 0
    go = 0
    pl = 0
    di = 0
    date = datetime.strptime("2019/01/01", "%Y/%m/%d")
    while date.year != 2020:
        if 0 <= date2value[date] < 10000:
            br += 1
        elif 10000 <= date2value[date] < 20000:
            si += 1
        elif 20000 <= date2value[date] < 50000:
            go += 1
        elif 50000 <= date2value[date] < 100000:
            pl += 1
        else:
            di += 1
        date += timedelta(days=1)

    answer = [br, si, go, pl, di]
    return answer


if __name__ == "__main__":
    pur = ["2019/01/01 5000", "2019/01/20 15000", "2019/02/09 90000"]
    print(solution(pur))
