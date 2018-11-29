def fizz_buzz(n):

    for i in range(1, n):
        entry = ''
        if i % 3 == 0:
            entry += 'fizz'
        if i % 5 == 0:
            entry += 'buzz'
        if i % 3 != 0 and i % 5 != 0:
            entry = i
        print(entry)


if __name__ == '__main__':
    fizz_buzz(50)
