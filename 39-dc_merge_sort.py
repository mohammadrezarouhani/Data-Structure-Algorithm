def merge(arr1, arr2):
    temp_arr = []
    rev_arr1 = arr1[::-1]
    rev_arr2 = arr2[::-1]

    while rev_arr1 and rev_arr2:
        if rev_arr1[-1] < rev_arr2[-1]:
            temp_arr.append(rev_arr1.pop())
        else:
            temp_arr.append(rev_arr2.pop())

    while rev_arr1:
        temp_arr.append(rev_arr1.pop())

    while rev_arr2:
        temp_arr.append(rev_arr2.pop())

    return temp_arr


def merge_sort(arr):
    length = len(arr)

    if len(arr) < 2:
        return arr
    else:
        left = merge_sort(arr[: length // 2]) 
        right = merge_sort(arr[length // 2 :]) 
        return merge(left, right)


print(merge_sort([2, 5, 9, 6, 7, 8, 15, 13, 12, 10]))
