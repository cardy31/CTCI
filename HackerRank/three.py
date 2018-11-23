
def main():
    n = usernameDisparity(['ababa', 'ababa'])
    print(n)


def usernameDisparity(inputs):
    total = []

    for username in inputs:
        current_str = username
        local_total = 0
        for i in range(0, len(username)):
            count = 0

            for i in range(0, len(current_str)):
                if current_str[i] == username[i]:
                    count += 1
                else:
                    break

            local_total += count
            current_str = current_str[1:]
        total.append(local_total)
    return total


if __name__ == "__main__":
    main()
