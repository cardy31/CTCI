def main():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print_matrix(rotate_matrix(matrix))


def rotate_matrix(matrix):
    n = len(matrix[0])

    for cycle in range(0, int(n / 2)):
        last_index = n - 1 - cycle

        for index in range(0, last_index):
            offset = index - cycle
            top = matrix[cycle][index]

            # Left -> Top
            matrix[cycle][index] = matrix[last_index - offset][cycle]

            # Bottom -> Left
            matrix[last_index - offset][cycle] = matrix[last_index][last_index - offset]

            # Right -> Bottom
            matrix[last_index][last_index - offset] = matrix[index][last_index]

            # Top -> Right
            matrix[index][last_index] = top

    return matrix


def print_matrix(matrix):
    for i in range(0, len(matrix)):
        print(matrix[i])


if __name__ == '__main__':
    main()
