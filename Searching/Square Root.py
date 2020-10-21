def square_root(num):
    beg, end, sqrt = 1, num, -1
    while beg <= end:
        mid = (beg + end)//2
        mid_square = mid * mid
        if mid_square == num:
            return mid
        elif mid_square > num:
            end = mid - 1
        else:
            beg = mid + 1
            sqrt = mid
    return sqrt


num = int(input('Enter a number: '))
print(f'Square root is {square_root(num)}')