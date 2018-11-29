def quicksort(arr, low_index, high_index):
    if low_index < high_index:
        pivot = partition(arr, low_index, high_index)
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
    arr = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    quicksort(arr, 0, len(arr) - 1)
    print(arr)
