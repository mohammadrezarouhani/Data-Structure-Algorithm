def quick_sort(arr):

    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr if i < pivot]
        greater = [i for i in arr if i > pivot]

        return quick_sort(less) + [pivot] + quick_sort(greater)
    

print(quick_sort([3,5,6,9,7,8,1,4,5,6,9,10,25,35]))
    