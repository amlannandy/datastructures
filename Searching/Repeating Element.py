def repeating_element(arr):
    slow = fast = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast:
            break
    slow = arr[0]
    while True:
        slow = arr[slow]
        fast = arr[fast]
        if slow == fast:
            break
    return slow

arr = list(map(int, input('Enter Array: ').split()))
print(f'Repeating element is {repeating_element(arr)}')