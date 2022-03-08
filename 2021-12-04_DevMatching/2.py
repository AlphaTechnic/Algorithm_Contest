import heapq
from heapq import *

txt2interval = dict()


def solution(n, recipes, orders):
    for recipe in recipes:
        txt, interval = recipe.split()
        txt2interval[txt] = int(interval)

    pq = []
    for i in range(n):
        heapq.heappush(pq, 0)

    for i, order in enumerate(orders):
        txt, time = order.split()
        time = int(time)

        l = time
        r = time + txt2interval[txt]

        finish_time = pq[0]
        if finish_time <= l:
            new_val = r
            heapq.heappop(pq)
            heapq.heappush(pq, new_val)
            if i == len(orders) - 1:
                return new_val
                # print(new_val)

        else:
            new_val = pq[0] + txt2interval[txt]
            heapq.heappop(pq)
            heapq.heappush(pq, new_val)
            if i == len(orders) - 1:
                return new_val
                # print(new_val)


if __name__ == "__main__":
    n = 3
    recipes = ["SPAGHETTI 3", "FRIEDRICE 2", "PIZZA 8"]
    orders = ["PIZZA 1", "FRIEDRICE 2", "SPAGHETTI 4", "SPAGHETTI 6", "PIZZA 7", "SPAGHETTI 8"]
    solution(n, recipes, orders)
