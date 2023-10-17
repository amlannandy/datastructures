def bubble_sort(arr):
  n = len(arr)
  for i in range(n - 1):
    for j in range(n - i - 1):
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp

n = int(input("Enter size of array: "))
arr = list(map(int, input("Enter array elements: ").split()))[:n]
bubble_sort(arr)
print("Sorted array is:", arr)