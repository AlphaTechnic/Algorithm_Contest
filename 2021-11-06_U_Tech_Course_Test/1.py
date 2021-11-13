# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(arr):
    # write your code in Python 3.6
    even_max = odd_max = 0
    for i in range(len(arr)):
        if arr[i] % 2 == 0 and arr[i] > even_max:
            even_max = arr[i]
        elif arr[i] % 2 == 1 and arr[i] > odd_max:
            odd_max = arr[i]

    return even_max + odd_max


if __name__ == "__main__":
    pass