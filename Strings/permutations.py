def main():
    myarr = [1, 2, 3]

    heaps(myarr, len(myarr), len(myarr))


def heaps(arr, size, n):
    if size == 1:
        print(arr)

    for i in range(0, size):
        heaps(arr, size-1, n)

        if size % 2 == 1:
            temp = arr[0]
            arr[0] = arr[size-1]
            arr[size-1] = temp

        else:
            temp = arr[i]
            arr[i] = arr[size-1]
            arr[size-1] = temp


if __name__ == '__main__':
    main()
