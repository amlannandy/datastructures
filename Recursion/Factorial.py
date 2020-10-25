# Non tail recursive
def get_fact(n):
    if n == 1 or n == 0:
        return 1
    return n * get_fact(n-1)

# tail recursive
def get_factorial(n, k):
    if n == 0 or n == 1:
        return k
    return get_factorial(n-1, k * n)

print(get_factorial(int(input('Enter num: ')), 1))