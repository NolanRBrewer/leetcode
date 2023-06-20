heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
# check area for every pair of lines
# if area of current pair is greater than previous replace the value


def max_area(heights: list[int]) -> int:
    largest_container = 0
    for index, line in enumerate(heights):

        for index_2, line_2 in enumerate(heights[index+1:]):

            width = index_2 + 1
            height = min([line, line_2])

            area = width * height

            if area > largest_container:
                largest_container = area
    return largest_container


print(max_area(heights))
