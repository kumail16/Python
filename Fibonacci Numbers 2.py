num = int (input('How may fibonacci numbers do you like to generate? '))
i = 1
if num == 0:
    fib = []
elif num == 1:
    fib = [1]
elif num == 2:
    fib = [1,1]
elif num > 2:
    fib = [1,1]
    while i < (num - 1):
        fib.append(fib[i] + fib[i-1])
        i += 1
print(fib)
