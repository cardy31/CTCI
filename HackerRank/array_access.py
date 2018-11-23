def main():
    arr = [1, 2, 3, 4]

    print(reverseArray(arr))


def reverseArray(arr):
    final = []
    for i in range(len(arr) - 1, -1, -1):
        final.append(arr[i])
    return final


if __name__ == "__main__":
    main()
