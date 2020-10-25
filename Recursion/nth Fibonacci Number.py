def get_fib(n):
    if n <= 1:
        return n
    return get_fib(n-1) + get_fib(n-2)

print(get_fib(int(input('Enter n: '))))