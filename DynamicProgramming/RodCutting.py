import sys


def cut_rod(price, n, depth):

    if n <= 0:
        return 0

    max_val = -sys.maxsize - 1

    for i in range(0, n):
        max_val = max(max_val, price[i] + cut_rod(price, n - 1 - i, depth + 1))

    return max_val


if __name__ == '__main__':
    arr = [1, 5, 8, 9, 10, 17, 17, 20]
    print('Max val is: ', cut_rod(arr, len(arr), 0))
