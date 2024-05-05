li = []


def calculate_sum(statement, target, calculation="", index=-1):
    global li

    if index == len(statement) - 1:
        if eval(calculation) == target:
            li.append(calculation)
        return 0
    elif index == 0:
        calculate_sum(statement, target, statement[index + 1], index + 1)
    else:
        calculate_sum(
            statement, target, calculation + "+" + statement[index + 1], index + 1
        )

        calculate_sum(
            statement, target, calculation + "-" + statement[index + 1], index + 1
        )

        calculate_sum(
            statement, target, calculation + "*" + statement[index + 1], index + 1
        )


calculate_sum("1234567891011", 512)
print(len(li))
