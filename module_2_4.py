
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
lenth = len(numbers)

for i in numbers:
    k = 0
    for j in range(1, lenth + 1):
        if i == 1:
            break
        elif i % j == 0:
            k = k + 1
            if i / j < 1:
                break
    if i == 1:
        continue
    if k == 2:
        primes.append(i)
    else:
        not_primes.append(i)


print('не простые числа: ' + str(not_primes))
print('простые числа: ' + str(primes))