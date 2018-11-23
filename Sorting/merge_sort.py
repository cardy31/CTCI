def main():
    alist = [54, 26, 93, 17, 77, 31, 44, 55, 20, 13]
    alist = merge_sort(alist)
    print(alist)


def merge_sort(alist):
    print("Split ", alist)
    if len(alist) == 1:
        return alist

    # Get midpoint
    mid = len(alist)//2

    # Split list at midpoint
    lefthalf = alist[:mid]
    righthalf = alist[mid:]

    lefthalf = merge_sort(lefthalf)  # Sort first half
    righthalf = merge_sort(righthalf)  # Sort second half

    return merge(lefthalf, righthalf)


def merge(lefthalf, righthalf):
    print('Merge {} {}'.format(lefthalf, righthalf))
    alist = []

    while lefthalf and righthalf:
        if lefthalf[0] > righthalf[0]:
            alist.append(righthalf.pop(0))
        else:
            alist.append(lefthalf.pop(0))

    while lefthalf:
        alist.append(lefthalf.pop(0))

    while righthalf:
        alist.append(righthalf.pop(0))

    return alist


if __name__ == '__main__':
    main()
