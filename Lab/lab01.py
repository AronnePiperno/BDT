def warmup(a,b):
    a = int(input('insert an integer: '))
    b = int(input('insert an integer: '))
    if a*b > 1000:
        return 'greater than 1000'
    else:
        return a*b


print(warmup(a,b))