def maxArea(heights):
    # Constraint check
    if len(heights) < 2:
        return 0

    curr_max = 0
    bottom = 0
    top = len(heights) - 1

    while top > bottom:
        curr_max = max(curr_max, (top - bottom) * min(heights[bottom], heights[top]))
        if heights[top] < heights[bottom]:
            top -= 1
        else:
            bottom += 1

    return curr_max


if __name__ == '__main__':
    arr = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(maxArea(arr))
