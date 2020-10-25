def sum_of_digits(n):
    if n < 10:
        return n
    return n%10 + sum_of_digits(n//10)

print(sum_of_digits(int(input('Enter a number: '))))