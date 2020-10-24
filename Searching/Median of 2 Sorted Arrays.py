def median_of_two_arrays(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    beg1, end1 = 0, n1
    while beg1 <= end1:
        i1 = (beg1 + end1)//2
        i2 = (n1 + n2 + 1)//2 - i1
        min1 = arr1[i1] if i1 != n1 else 10000
        max1 = arr1[i1-1] if i1 != 0 else -10000
        min2 = arr2[i2] if i2 != n2 else 10000
        max2 = arr2[i2-1] if i2 != 0 else -10000
        if max1 <= min1 and max2 <= min2:
            if (n1 + n2) % 2 == 0:
                return (max(max1, max2) + min(min1, min2))/2
            else:
                return max(max1, max2)
        elif max1 > min2:
            end1 = i1 - 1
        else:
            beg1 = i1 + 1
    return -1

arr1 = list(map(int, input('Enter 1st Array: ').split()))
arr2 = list(map(int, input('Enter 2nd Array: ').split()))
print(f'Median of merged sorted array is {median_of_two_arrays(arr1, arr2)}')