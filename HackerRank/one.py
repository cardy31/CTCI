import itertools


def main():
    variantsCount(3, 2, 3, 3, 2, 15)


def variantsCount(n, s0, k, b, m, a):

    s = []
    s.append(s0)

    for i in range(1, n):
        number = (((k * s[i - 1] + b) % m) + 1 + s[i - 1])
        s.append(number)

    new_list = itertools.combinations(s, 2)

    total = 0
    for element in new_list:
        if element[0] * element[1] <= a:
            total += 2

    for element in s:
        if element * element <= a:
            total += 1


    return total


if __name__ == "__main__":
    main()
