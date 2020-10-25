def firstN(num):
    if num == 0:
        return 0
    return num + firstN(num-1)

print(firstN(int(input('Enter n: '))))