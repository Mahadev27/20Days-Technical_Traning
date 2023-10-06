def insertion_sort(arr):
    for i in range(1, len(arr)):
        current_value = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value
my_list = list(map(int, input('Enter an array:').split(',')))
insertion_sort(my_list)
print(my_list)
