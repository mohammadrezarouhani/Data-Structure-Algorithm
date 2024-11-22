


def devide_farm(length,width):
    if length % width ==0:
        return width
    else:
        return devide_farm(width,length%width)



print(devide_farm(1680,640))