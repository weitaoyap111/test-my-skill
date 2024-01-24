import time

def is_prime(n):
    if n <= 1:
        return False
    for x in range(2, int(n/2)+1):
        if n % x == 0:
            return False
    else:
        return True

def divide(number):
    start = time.time()
    next_number = 2
    list_p = []

    while number != 1:
        if is_prime(next_number):
            if number % next_number == 0:
                number /= next_number
                list_p.append(next_number)
        next_number += 1
        if number < next_number:
            break
        if is_prime(number):
            list_p.append(number)
            break

    end = time.time()
    print(end - start)
    return list_p

print(divide(1234567890))
# result
# 0.1359236240386963
# [2, 3, 5, 3607, 3803]
