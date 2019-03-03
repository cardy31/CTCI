def main(arr, target):

    left = 0
    right = len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > target:
            right = mid
        elif arr[mid] < target:
            left = mid
        else:
            return mid


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    res = main(arr, 4)
    print(res)
