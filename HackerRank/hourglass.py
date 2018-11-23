def main():
    arr = [[1, 1, 1, 0, 0, 0], [0, 1, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0],
           [0, 0, 2, 4, 4, 0], [0, 0, 0, 2, 0, 0], [0, 0, 1, 2, 4, 0], [0, 0, 1, 2, 4, 0]]

    arr = [[-1, -1, 0, -9, -2, -2], [-2, -1, -6, -8, -2, -5], [-1, -1, -1, -2, -3, -4]]

    print(hourglassSum(arr))


def hourglassSum(arr):
    n = len(arr)
    m = len(arr[0])
    max = -9

    for i in range(0, n - 2):
        for j in range(0, m - 2):
            print("i: {}, j: {}".format(i, j))
            temp = getHourglassFromPoint(arr, i, j)
            if temp > max:
                max = temp
    return max


def getHourglassFromPoint(arr, n, m):
    sum = 0
    sum += arr[n][m] + arr[n][m + 1] + arr[n][m + 2]
    sum += arr[n + 1][m + 1]
    sum += arr[n + 2][m] + arr[n + 2][m + 1] + arr[n + 2][m + 2]

    return sum


if __name__ == "__main__":
    main()