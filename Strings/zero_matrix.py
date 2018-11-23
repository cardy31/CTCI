def main():
    matrix = [[1, 2, 3], [4, 0, 6], [7, 8, 9]]
    print_matrix(matrix)
    print()
    print_matrix(zero_matrix(matrix))


def zero_matrix(matrix):
    if len(matrix) == 0:
        return False

    rows = []
    columns = []
    n = len(matrix)
    m = len(matrix[0])

    for i in range(0, n):
        for j in range(0, m):
            if matrix[i][j] == 0:
                if i not in rows:
                    rows.append(i)
                if j not in columns:
                    columns.append(j)

    for row in rows:
        for i in range(0, m):
            matrix[row][i] = 0

    for column in columns:
        for i in range(0, n):
            matrix[i][column] = 0

    return matrix


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    main()