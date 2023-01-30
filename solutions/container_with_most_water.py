height = [1, 8, 6, 2, 5, 4, 8, 3, 7]


def max_area(height: list[int]) -> int:
    size = len(height) - 1
    # hold on to each line's height
    line_1, line_2 = 0, size
    # the maximum width
    max_width = size
    area = 0
    # range(start, stop, step)
    # start at the end work backwards until you hit the begining
    # working through you calculate area as you go
    for width in range(max_width, 0, -1):

        # determine which line is shorter and calculate area off lesser value
        if height[line_1] < height[line_2]:
            # determine if the area is greater than previously found
            # if so replace value
            area = max(area, width * height[line_1])
            # move left pointer in one line
            line_1 += 1
        else:
            area = max(area, width * height[line_2])
            # move right pointer in one line
            line_2 -= 1

    return area


print(max_area(height))
