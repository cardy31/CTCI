def quicksort(arr, low_index, high_index):
    print('low: {}, high: {}'.format(low_index, high_index))
    if low_index < high_index:
        pivot = partition(arr, low_index, high_index)
        print('pivot:', pivot)
        print()
        quicksort(arr, low_index, pivot - 1)
        quicksort(arr, pivot + 1, high_index)


def partition(arr, low_index, high_index):
    pivot = arr[high_index]

    i = low_index - 1

    for j in range(low_index, high_index):
        if arr[j] <= pivot:
            i += 1
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
    temp = arr[i + 1]
    arr[i + 1] = arr[high_index]
    arr[high_index] = temp

    return i + 1


if __name__ == '__main__':
    alist = [8, 10, 8, 7, 5, 12]
    quicksort(alist, 0, len(alist) - 1)
    print(alist)
