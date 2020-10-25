def dec_to_bin(num):
    if num == 0:
        return
    dec_to_bin(num//2)
    print(num%2, end='')

dec_to_bin(int(input('Enter number: ')))