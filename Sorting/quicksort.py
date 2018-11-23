def main():
    alist = [13, 9, 8, 5, 1]
    print(alist)
    quicksort(alist, 0, len(alist) - 1)
    print(alist)


def quicksort(arr, low_index, high_index):

    if low_index < high_index:
        pivot = partition(arr, low_index, high_index)
        quicksort(arr, low_index, pivot - 1)
        quicksort(arr, pivot+1, high_index)


def partition(arr, low_index, high_index):
    print(arr)
    pivot = arr[high_index]

    i = low_index - 1

    for j in range(low_index, high_index):
        # print('Pivot is: ', )
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
        # print(arr)
    temp = arr[i + 1]
    arr[i + 1] = arr[high_index]
    arr[high_index] = temp
    print(arr)
    return i + 1


if __name__ == '__main__':
    main()
