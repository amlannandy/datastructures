def print_n_to_1(n):
    if n == 0:
        return
    print(n, end=' ')
    print_n_to_1(n-1)

print_n_to_1(int(input('Enter n: ')))
        