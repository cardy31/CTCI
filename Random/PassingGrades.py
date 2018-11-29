# Puts all passing grades at the front of array, and all failing grades at back
# Only has to track 'dead' space, ie. how many elements have been moved to the end of the array


def passing_grades(arr):
    dead = 0
    last_index = len(arr) - 1
    i = 0
    while i < len(arr) - dead:
        if arr[i] < 50:
            temp = arr[i]
            arr[i] = arr[last_index - dead]
            arr[last_index - dead] = temp
            dead += 1
            if arr[i] >= 50:
                i += 1
        else:
            i += 1
        print(len(arr) - dead)


if __name__ == '__main__':
    alist = [10, 52, 68, 33, 79, 81, 90, 54, 11]
    passing_grades(alist)
    print(alist)
