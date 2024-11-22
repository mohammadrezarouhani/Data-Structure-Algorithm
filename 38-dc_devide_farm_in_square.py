def divide_farm(length, width):

    if length % width == 0:
        return width
    else:
        return (
            divide_farm(width, length % width)
            if length > width
            else divide_farm(length, width % length)
        )
