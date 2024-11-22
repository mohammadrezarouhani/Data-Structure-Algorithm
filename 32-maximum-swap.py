def maximum_swap(number):
    target = 0
    num_list = list(str(number))
    num_mapper = {num: index for index, num in enumerate(num_list)}

    for i, n in enumerate(num_list):
        for integer in range(9, int(n), -1):
            if target := num_mapper.get(str(integer), -1):
                if target > i:
                    temp = num_list[i]
                    num_list[i] = num_list[target]
                    num_list[target] = temp
                    return int("".join(num_list))


print(maximum_swap(9623))
