from collections import Counter
import operator


def main():
    degreeOfArray([1, 2, 1, 3, 2])


def degreeOfArray(arr):
    counter = Counter(arr)
    degree = max(counter.values())

    keys = []
    values = []

    highest = counter.most_common()[0][1]
    for i in counter.most_common():
        if i[1] < highest:
            break
        keys.append(i[0])
        values.append(i[1])

    print(keys)
    print(values)
    print(degree)

    count = 0

    candidates = []

    for k in range(0, len(keys)):
        value = values[k]
        for i in range(0, len(arr)):
            if arr[i] != value:
                continue
            count = 1
            for j in range(i + 1, i + degree - 1):
                if j > len(arr) - 1:
                    break
                if arr[j] == value:
                    count += 1
                if count == degree:
                    print("append {}:{}".format(i, i + degree))
                    candidates.append(arr[i:i + degree])
                    break

    print(candidates)

    return min(candidates)


if __name__ == "__main__":
    main()
