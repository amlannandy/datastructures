def selection_sort(arr):
  n = len(arr)
  for i in range(n-1):
    min_index = i
    for j in range(i+1, n):
      if arr[j] < arr[min_index]:
        min_index = j
    if min_index != i:
      temp = arr[i]
      arr[i] = arr[min_index]
      arr[min_index] = temp
    print(arr)

n = int(input("Enter array size: "))
arr = list(map(int, input("Enter array elements: ").split()))
selection_sort(arr)
print("Sorted array is:", arr)