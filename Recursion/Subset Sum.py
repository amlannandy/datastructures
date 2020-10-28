def subset_sum(arr, n, target):
    if n == 0:
        return 1 if target == 0 else 0
    return subset_sum(arr, n-1, target) + subset_sum(arr, n-1, target - arr[n-1])

arr = list(map(int, input('Enter array: ').split()))
target = int(input('Enter target: '))
print(f'{subset_sum(arr, len(arr), target)} subsets found.')
