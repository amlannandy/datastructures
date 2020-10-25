def print_1_to_n(n):
    if n == 0:
        return
    print_1_to_n(n-1)
    print(n, end=' ')

# using tail recursion
def one_to_n(n, k):
    if n == 0:
        return
    print(k)
    one_to_n(n-1, k+1)

print_1_to_n(int(input('Enter n: ')))