def main():

    for i in range(0, 100):
        print(fib(i))


# 0, 1, 1, 2, 3, 5, 8, 13...
def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


if __name__ == '__main__':
    main()
