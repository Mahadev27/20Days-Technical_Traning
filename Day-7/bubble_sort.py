def bubble_sort(arr):
    n = len(arr)
    swapped = True
    while swapped:
        swapped = False
        i = 0
        while i < n - 1:
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
            i += 1
    return arr
arr = list(map(int, input('Enter an array:').split(',')))
res = bubble_sort(arr)
print(res)
