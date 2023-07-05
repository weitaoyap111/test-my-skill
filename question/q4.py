import time
import math
test_number = 159999962400002173
factor_list = []
factor_list2 = []


def find_factor():
    for x in range(2, math.isqrt(test_number+1)):
        if test_number % x == 0:
            factor_list.append(x)


start_time = time.time()
find_factor()
end_time = time.time()
print(factor_list)
print("total time: ", end_time - start_time)
"""
start_time = time.time()
find_factor2()
end_time = time.time()
print(factor_list2)
print("total time: ", end_time - start_time)
"""


