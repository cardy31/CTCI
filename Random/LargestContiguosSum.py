def largest_contiguous_sum(int_array):
    i = 0
    j = len(int_array) - 1

    curr_max = -100000000000000

    while i < j:
        total = sum_array(int_array, i, j)
        if total > curr_max:
            curr_max = total

        if total - int_array[i] > total - int_array[j]:
            i += 1
        else:
            j -= 1

    return curr_max


def sum_array(arr, start, end):
    total = 0
    for i in range(start, end + 1):
        total += arr[i]

    return total


if __name__ == '__main__':
    print(largest_contiguous_sum([-10, 2, 3, -2, 0, 5, -15]))
