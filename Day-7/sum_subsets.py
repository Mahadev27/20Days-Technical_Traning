def find_all_subsets(arr, target_sum):
    def find_subsets(subset, index, current_sum):
        if current_sum == target_sum:
            result.append(subset[:])
            return
        if index == len(arr) or current_sum > target_sum:
            return
        subset.append(arr[index])
        find_subsets(subset, index + 1, current_sum + arr[index])
        subset.pop()
        find_subsets(subset, index + 1, current_sum)
    result = []
    find_subsets([], 0, 0)
    return result
#arr = list(map(int,input('Enter an array: ').split(',')))
arr=[6,8,9,5,4,3,26,2]
target_sum = int(input('Enter sum: '))
if target_sum>min(arr):
    result = find_all_subsets(arr, target_sum)
    if result:
        for subset in result:
            print(subset)
    else:
        print("No subsets found with sum", target_sum)
else:
    print("Target sum should be greater than 1")