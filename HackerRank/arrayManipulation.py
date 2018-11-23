
def main():
    queries = [[1, 2, 100], [2, 5, 100], [3, 4, 100]]

    print(arrayManipulation(5, queries))


def arrayManipulation(n, queries):
    arr = [0] * n
    max_val = -10000
    for query in queries:
        for i in range(query[0] - 1, query[1]):
            arr[i] += query[2]
            if max_val < arr[i]:
                max_val = arr[i]
        print(arr)
    return max_val


if __name__ == "__main__":
    main()